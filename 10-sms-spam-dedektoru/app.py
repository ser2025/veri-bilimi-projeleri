import streamlit as st
import pandas as pd
import numpy as np
import joblib
import neattext as nfx

st.set_page_config(page_title='SMS Spam Dedektörü',page_icon='📩',layout='centered')
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&display=swap');
html, body, [class*="css"] {font-family:'IBM Plex Sans',sans-serif;}
h1 {font-weight:600; letter-spacing:-0.5px;}
.balon {background:#FFFFFF; border:1px solid #D5DEE8; border-radius:18px 18px 18px 4px;
        padding:14px 18px; margin:8px 0 18px 0; line-height:1.9; max-width:620px; font-size:1.02rem;}
mark.spam {background:#F8D5D1; color:#8C1D17; border-radius:4px; padding:1px 4px;}
mark.ham {background:#D2EEDF; color:#1B5B3D; border-radius:4px; padding:1px 4px;}
</style>
""",unsafe_allow_html=True)

# 1) Notebook'ta eğitilip kaydedilen model: CountVectorizer + Naive Bayes
model=joblib.load('spam_model.pkl')
vect=model.named_steps['Vect']
nb=model.named_steps['Classifier']
spam_sira=list(model.classes_).index('spam')

# 2) Her kelimenin spam puanı: spam'de görülme olasılığının log'u eksi normal mesajda görülme olasılığının log'u
puanlar=pd.Series(nb.feature_log_prob_[spam_sira]-nb.feature_log_prob_[1-spam_sira],index=vect.get_feature_names_out())

# 3) Eğitimdekiyle aynı temizlik
def temizle(metin):
    return metin.str.lower().apply(nfx.remove_stopwords).apply(nfx.remove_puncts).apply(nfx.remove_special_characters)

st.title('SMS Spam Dedektörü')
st.write('Bir SMS yapıştır; model spam olup olmadığını ve hangi kelimelerin bu kararı etkilediğini göstersin.')

tek,toplu=st.tabs(['Tek mesaj','Toplu kontrol (CSV)'])

with tek:
    mesaj=st.text_area('Mesaj','Congratulations! You won a FREE iPhone. Call 08001234567 now to claim your prize',height=110)
    temiz=temizle(pd.Series([mesaj]))
    karar=model.predict(temiz)[0]
    olasilik=float(model.predict_proba(temiz)[0][spam_sira])

    kelimeler=pd.Series(mesaj.split())
    kelime_puani=temizle(kelimeler).map(puanlar).fillna(0)
    guvenli=kelimeler.str.replace('<','&lt;').str.replace('>','&gt;') # HTML etiketi gibi görünen yazılar bozulmasın
    isaretli=np.where(kelime_puani>1.5,'<mark class="spam">'+guvenli+'</mark>',
                      np.where(kelime_puani<-1.5,'<mark class="ham">'+guvenli+'</mark>',guvenli))
    st.markdown('<div class="balon">'+' '.join(isaretli)+'</div>',unsafe_allow_html=True)

    {'spam':st.error,'ham':st.success}[karar]({'spam':'Spam. Spam olasılığı %'+str(round(olasilik*100,1)),
                                               'ham':'Normal mesaj. Spam olasılığı %'+str(round(olasilik*100,1))}[karar])
    st.progress(olasilik)
    st.caption('Kırmızı işaretli kelimeler spam mesajlarda, yeşil işaretliler normal mesajlarda belirgin şekilde daha sık geçiyor.')

    etkili=pd.DataFrame({'Kelime':kelimeler,'Spam puanı':kelime_puani.round(2)}).sort_values('Spam puanı',ascending=False)
    st.dataframe(etkili[etkili['Spam puanı']!=0].head(6),hide_index=True,width='stretch')

with toplu:
    st.write('`text` sütunu olan bir CSV yükle. Dosya yüklenmezse 8 örnek mesaj kontrol edilir.')
    dosya=st.file_uploader('CSV dosyası',type='csv') or 'ornek_mesajlar.csv'
    tablo=pd.read_csv(dosya)
    tablo['Tahmin']=model.predict(temizle(tablo['text']))
    tablo['Spam olasılığı']=model.predict_proba(temizle(tablo['text']))[:,spam_sira].round(3)
    sol,orta,sag=st.columns(3)
    sol.metric('Mesaj',len(tablo))
    orta.metric('Spam',int((tablo['Tahmin']=='spam').sum()))
    sag.metric('Normal',int((tablo['Tahmin']=='ham').sum()))
    st.dataframe(tablo.sort_values('Spam olasılığı',ascending=False),hide_index=True,width='stretch')
    st.download_button('Sonuçları CSV olarak indir',tablo.to_csv(index=False).encode('utf-8'),'tahminler.csv','text/csv')

with st.expander('Model hakkında'):
    st.write('5.158 SMS (tekrarlar silindikten sonra) ile eğitildi. Test verisinde üç model karşılaştırıldı:')
    st.dataframe(pd.DataFrame({'Model':['Naive Bayes','TF-IDF + SVC','Random Forest'],'Accuracy':[0.983,0.976,0.968],'Spam F1':[0.927,0.892,0.855]}),hide_index=True)
    st.write('Seçilen model Naive Bayes: test verisindeki 128 spam mesajın 114\'ünü yakaladı, 904 normal mesajın sadece 4\'üne yanlışlıkla spam dedi.')
