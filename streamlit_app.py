import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe
import time

def period_counter(list1,list4,n):
    index = list1.index(n)
    per=list4[index]
    return per


newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid orange;
                    border-radius:15px;
                    margin-top:67px;
                }
                .css-6awftf.e19lei0e1{ display:none;}

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
                .css-1cpxqw2.edgvbvh5:focus{background-color:white;
                    color: orange;
                    font-weight:bold;
                    border:3px solid orange;

                }
            
            </style>
            <body> 
            </body
        """
st.markdown(newhtml,unsafe_allow_html=True)


# names = ['MARIA	TERZI','Στεριανή Αβράμη','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','Μαρία Αγάθου']
# usernames = ['Maria-terzi@hotmail.com','stella-a88@hotmail.com','depi1970@hotmail.com','magathou@hotmail.com']
# passwords = ['tSYcA8GPCJ','hj2cJpZLXG','u46UXerHf9','pJH9CA7L2g']

html_logo = "<img style='display:block; margin-left:auto; margin-right:auto; text-align:center;' src='http://inclusiveeducation.eu/wp-content/uploads/2021/03/logoiam400x400.png'  width=300 height=300>"



st.markdown(html_logo, unsafe_allow_html=True)


names=['ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ', 'ΜΑΡΙΑ - ΕΙΡΗΝΗ ΓΑΛΕΡΑΚΗ', 'ΚΟΥΛΑ ΑΜΠΕΛΙΟΤΗ', 'ΕΙΡΗΝΗ ΑΝΑΤΣΟΥΤΣΟΥΛΑ', 'ΤΑΤΙΑΝΑ ΕΛΕΟΝΩΡΑ ΑΝΑΓΝΩΣΤΙΔΟΥ', 'ΕΥΓΕΝΙΑ ΤΡΑΓΑΚΗ', 'ΣΠΥΡΙΔΩΝ ΒΑΛΒΗΣ', 'ΣΟΦΙΑ ΓΙΔΑΡΗ', 'ΔΗΜΗΤΡΗΣ ΑΡΒΑΝΙΤΗΣ', 'ΠΑΝΑΓΙΩΤΑ ΒΑΣΙΛΕΙΟΥ', 'ΕΜΜΑΝΟΥΕΛΑ ΒΑΣΙΛΕΙΑΔΗ', 'ΜΑΡΙΑ ΓΟΥΡΓΙΩΤΗ', 'ΕΛΠΙΔΑ ΓΟΥΚΟΥ', 'ΜΑΡΙΑ ΤΕΡΖΟΥΔΗ', 'ΓΕΩΡΓΙΑ ΒΕΛΟΥΔΟΥ', 'ΜΑΡΙΑ ΤΕΡΖΗ', 'ΜΑΡΙΑ ΓΕΩΡΓΟΠΟΥΛΟΥ', 'ΒΑΣΣΟ ΑΝΔΡΟΥΤΣΟΥ', 'ΧΡΙΣΤΙΝΑ ΑΛΜΠΑΝΗ', 'ΘΕΟΔΩΡΑ ΓΚΟΥΝΑ', 'ΜΑΡΙΑ ΑΓΑΘΟΥ', 'ΑΛΕΞΙΟΣ ΑΡΦΑΝΗΣ', 'ΕΥΑΓΓΕΛΙΑ ΒΑΡΣΑΜΑ', 'ΧΡΗΣΤΙΝΑ ΒΟΥΛΓΑΡΙΔΟΥ', 'ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ', 'ΑΙΚΑΤΕΡΙΝΗ ΓΚΑΓΚΑΛΗ', 'ΑΛΕΞΑΝΔΡΑ ΑΛΤΙΠΑΡΜΑΚΗ', 'ΛΟΥΙΖΑ ΑΛΕΞΙΑΔΟΥ', 'ΒΕΖΑΣΗΣ ΕΥΘΥΜΙΟΣ', 'ΕΛΛΗ ΑΓΓΕΛΑΚΟΠΟΥΛΟΥ', 'ΔΕΣΠΟΙΝΑ ΧΑΤΖΗΔΡΟΣΟΥ', 'ΒΑΣΙΛΙΚΗ ΛΑΖΟΥ', 'ΑΝΔΡΙΑΝΑ ΔΕΛΕΓΚΟΥ', 'ΑΠΟΣΤΟΛΙΑ ΠΛΙΑΣΣΑ', 'ΑΝΑΣΤΑΣΙΑ ΧΑΤΖΗΓΕΩΡΓΙΟΥ', 'ΑΛΙΚΗ ΒΑΒΟΥΓΥΙΟΥ ', 'ΜΕΛΙΝΑ ΑΛΕΞΙΑΔΟΥ', 'ΤΣΑΡΟΥΧΑΣ ΝΕΚΤΑΡΙΟΣ', 'ΜΠΟΤΣΩΛΗ ΑΙΚΑΤΕΡΙΝΗ', 'Ιωάννα Μιχαλοπούλου', 'Κατερίνα Μεργιάννη', 'ΕΛΕΝΗ ΜΑΡΓΑΡΙΤΗ', 'ΙΩΑΝΝΑ ΡΕΙΖΟΠΟΥΛΟΥ', 'ΝΙΚΟΛΑΟΣ ΠΑΠΑΓΓΕΛΟΠΟΥΛΟΣ', 'ΠΗΝΕΛΟΠΗ ΚΑΡΑΣΙΜΟΥ', 'Ελευθερία Κουμπουρλή', 'ΘΩΜΑΗ ΣΙΣΚΟΥ', 'Αλεξάνδρα Μωράτη', 'Χρυσούλα Παλαιολόγου', 'Κλεοπάτρα Χύτα', 'Χρυσαφένια Δεμέτη', 'ΣΥΜΕΛΑ ΤΣΑΟΥΣΟΓΛΟΥ', 'Δέσποινα Μαρία Σέργη', 'Αλέξανδρος Τάτσης', 'ΙΩΑΝΝΑ ΚΩΝΣΤΑΝΤΙΝΙΔΟΥ', 'Δήμητρα Χανδόλια', 'ΠΑΝΑΓΙΩΤΑ ΜΠΟΖΩΝΗ', 'ΟΥΡΑΝΙΑ ΦΑΝΟΥΡΑΚΗ', 'Σταυρούλα Λιβιτσάνου', 'ΑΓΛΑΪΑ ΝΙΚΟΛΟΠΟΥΛΟΥ', 'Στεργιανή Κατσιόλα', 'ΦΩΤΕΙΝΗ ΜΗΛΙΑΡΗ', 'ΑΡΤΕΜΙΣ ΜΑΚΡΗ', 'Γεώργιος Θεμελίδης', 'Πετρούλα Λιάκου', 'ΣΤΥΛΙΑΝΗ ΦΑΡΜΑΚΗ', 'Ελlένη Κοκκίου', 'ΝΑΛΜΠΑΝΤΗ ΔΗΜΗΤΡΑ', 'Ελένη Τσώτσου', 'Θεονύμφη Μπουχαλάκη', 'ΕΥΦΗΜΙΑ ΟΙΚΟΝΟΜΙΔΟΥ', 'Όλγα Σουρβίνου', 'ΔΗΜΗΤΡΙΟΣ ΠΑΝΤΕΛΑΚΗΣ', 'Ρεϊχάν Κιοσέ']
usernames=['labrianatsiak@icloud.com', 'nikosmariagr@hotmail.com', 'kampel85@yahoo.gr', 'spaeirhnh@hotmail.com', 'tatianapsychology@yahoo.gr', 'eugenia.tragaki@gmail.com', 'nsvalv@gmail.com', 'sofiagidari@yahoo.gr', 'darv009@hotmail.com', 'vgiota83@hotmail.com', 'emmavasi76@gmail.com', 'maria.gr.bl@hotmail.com', 'elpidagoukou@yahoo.gr', 'terzoydi@gmail.com', 'tzovel72@yahoo.gr', 'maria-terzi@hotmail.com', 'mgeorgopoulou@gmail.com', 'vandrout@yahoo.gr', 'christina.albani@yahoo.gr', 'theodoragouna@gmail.com', 'magathou@hotmail.com', 'alexiosarfanis@gmail.com', 'lillyvarsama@yahoo.com', 'voulgaridou.christina@gmail.com', 'depi1970@hotmail.com', 'kgkagkali@gmail.com', 'alexandralt@yahoo.com', 'louiza.alex@gmail.com', 'efthymis.v@gmail.com', 'elliaggel@gmail.com', 'deppy.h@hotmail.com', 'lazouvaso@yahoo.gr', 'delegouandriana@yahoo.gr', 'litsapliassa@gmail.com', 'anastasiachatz3012@gmail.com', 'alikakiv_1986@hotmail.com', 'melinalexiadou@gmail.com', 'nectsarou@yahoo.gr', 'botsoli@yahoo.gr', 'joannamixalo@yahoo.gr', 'katmer2207@gmail.com', 'elenaki_m@yahoo.gr', 'reizjoanna@gmail.com', 'drnjp@hotmail.com', 'pinelopimesag@gmail.com', 'ekoumpourli@gmail.com', 'thomiesis@gmail.com', 'antamorati@gmail.com', 'chrisoula_pal@hotmail.com', 'kleopatra202008@hotmail.com', 'xryfede@hotmail.com', 'tsaousamel@hotmail.com', 'debbiemariasergi@gmail.com', 'alextts84@gmail.com', 'gianna_konsta1@yahoo.gr', 'dimitisdimitra@gmail.com', 'panagiwtamp@gmail.com', 'raniafanour@hotmail.com', 'loriliv@hotmail.com', 'lia.nikolomi@gmail.com', 'stergianikats@yahoo.com', 'feniamili@hotmail.com', 'stylianosmakris@gmail.com', 'giorgos.themelidis@gmail.com', 'lpenny20111@gmail.com', 'stellariafarmaki@gmail.com', 'elenikok756@gmail.com', 'naldimitra1974@gmail.com', 'elenits2001@gmail.com', 'theonhmp@gmail.com', 'efioikonomidou@gmail.com', 'olgasourv121993@yahoo.gr', 'sioteiri@hotmail.gr', 'reyhankiose@windowslive.com']
passwords=['kKw63vspMq', 'AV2wPELFZS', 'BK259LtGwu', 'a6BzbdXRJu', 'mLTcrCs6a9', 'Jv37HCYAMX', 'j8m7Dn4VHQ', 'AXJLQHhw7d', 'ZUc9n2gWVp', 'Hvuk4aspx7', 'MLVTdK26SB', 'UpZcq6hKTC', 'paT7jEgSAw', 'eH6ZDwbk2N', 'Wzp96ykNeD', 'tSYcA8GPCJ', 'w3XjgRETsL', 'Hy26wLYmzk', 'GsBEYywW9n', 'TpSe6atkf2', 'pJH9CA7L2g', 'L4UWEuD8MA', 'Q2GTuYE8ch', 'xcA43GJWaf', 'u46UXerHf9', 'Nz58pmgUDF', 'prF4k9VXb2', 'E8L4MjXsWe', 'UxYV7bNfv4', 'Aax5Xe3pTK', 'RTFtj7Vg3x', 'X94bWctMj5', 'TEahK53skD', 'YFDHf4cB8n', 'jPsvBFte7z', 'ZuAf4sPJUw', 'wWgcxYk7M2', 'M5Dr8aJxhy', 'zPeaCyw3nq', 'xK6fdCh957', 'FmLV3yETru', 'Luh5DAsG3z', 'C9LAyaVnG4', 'QgK64HvXbs', 'vk3d548UTh', 'j3yW5wTMmX', 'Kaj7SLhUgb', 's7nCSxg8D6', 'Ud3aV4KxDv', 'gWEu5mP9af', 'KEg9Lf5acb', 'mJ7S4fRDKG', 'VLnz95ATF3', 'YjRHyW2kU3', 'YrSkWj8wXp', 'f2qecKdsgR', 'zLch3KQ4Yg', 'S4Gn9NEpjz', 'r36bCMyk2K', 'CRnKGw3Lmx', 'gECXFsJ2zV', 'RxHtjBkG4g', 'meCVcW3jGp', 'DXMWE6sgGn', 'TMvU6FnpPx', 'gj7KYfCXLc', 'sj382GLBMS', 'tv8q5TmKzF', 'K8scC4kJ3v', 'vy2BsQg6Wz', 'mRDFz8W43b', 'Ffr8nHcKYp', 'DsS32w85u7', 'ntUAeEV3WD']
periods=['11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου']



# hashed_passwords = stauth.hasher(passwords).generate()
hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)


name, authentication_status = authenticator.login('Login','main')



if authentication_status:
        # newhtml="""
        #     <!DOCTYPE html>
        #     <header></header>
        #     <style>
        #        .css-1v3fvcr{background: rgb(34,193,195);
        #         background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
        #         }
        #         div.css-nlntq9.e16nr0p33 p{background-color:white;
        #         }
        #         .css-nlntq9.e16nr0p33{}
        #         .block-container.css-12oz5g7.egzxvld2{background-color:white;
        #             border:5px solid black;
        #             border-radius:15px;
        #             margin-top:67px;
        #         }

        #         .title{}
        #         .css-1cpxqw2.edgvbvh5{background-color:orange;
        #             color: white;
        #         }
            
        #     </style>
        #     <body> 
        #     </body
        # """

        html2="""
            <!DOCTYPE html>
            <header></header>
            <style>
               
            
            </style>
            <body> 
                <ul>
                    <li>Πατήστε στο κουμπί "δημιουργία πιστοποιητικού" για να δημιουργήσετε το πιστοποιητικό σας</li>
                    <li>Αφού δημιουργήσετε το πιστοποιητικό σας, πατήστε στο κουμπί "παραλαβή πιστοποιητικού" για να κατεβάσετε το πιστοποιητικό σας</li>
                </ul>
            </body
        """
        html3="""
            <!DOCTYPE html>
            <header></header>
 
            <body> 
               <h3 style="text-align:center;">🎓 Εκτυπώστε το πιστοποιητικό σας</h3>
            </body
        """
        # st.markdown(newhtml,unsafe_allow_html=True)
        st.write('Καλησπέρα, *%s*' % (name))
        perds=period_counter(names,periods,name)

        # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
        st.markdown(html3,unsafe_allow_html=True)

        st.markdown(html2,unsafe_allow_html=True)

        left, right = st.columns(2)

        # right.write("Here's the template we'll be using:")

        right.image("http://inclusiveeducation.eu/wp-content/uploads/2022/04/template.png", width=300)

        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")

        
        # left.write("Fill in the data:")
        form = left.form("template_form")
        student = name
        course="Report Generation in Streamlit"
        grade = 100
        period=perds
        submit = form.form_submit_button("Δημιουργία πιστοποιητικού")
        
        if submit:
            html = template.render(
                student=student,
                course=course,
                period=period,
                grade=f"{grade}/100",
                date=date.today().strftime("%B %d, %Y"),
            )

            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Παραλαβή πιστοποιητικού",
                data=pdf,
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')