import mysql.connector
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout #plus flexible et libre
from kivy.uix.boxlayout import BoxLayout #ligne ou en colonne.
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup # aficher les messages d'erreur avertissements , pour demander à lutilisateur de confirmer une action
from kivy.uix.spinner import Spinner # slct une dans une list 
from kivy.uix.screenmanager import ScreenManager, Screen # plusieurs ecran pages 
from kivy.uix.gridlayout import GridLayout # pour stryctere les donnnes ... 
from kivy.uix.scrollview import ScrollView # n7taj grand ecran lles donner li 3Ndi 
import re  # re.fullmatch(pattern, string)


wilayas = [
    "Alger", "Oran", "Blida", "Constantine", "Annaba", "Tlemcen", "Batna", "Sétif", "Chlef",
    "Djelfa", "Tiaret", "Biskra", "Skikda", "Tipaza", "Tizi Ouzou", "Bejaia", "M'sila", "Mascara",
    "Saida", "Sidi Bel Abbes", "El Oued", "El Tarf", "Souk Ahras", "Khenchela", "Oum El Bouaghi",
    "Bouira", "Béchar", "Boumerdes", "Guelma", "Médéa", "Laghouat", "Mostaganem", "Aïn Defla",
    "Kairouan", "Tindouf", "Tamanrasset", "El Bayadh", "Ghardaïa", "Aïn Témouchent", "Ouargla"
]

# connecter au base de donner 
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="",       
            database="my_database"  
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# fonctione pour inserer les donner 
def insert_data(nom, prenom, email, phone, nin, birth_date, wilaya, commune, ccp_account, ccp_code):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO users (Nom, Prénom, AdresseMail, NuméroDeTéléphone, NIN, DateDeNaissance, Wilaya, Commune, CCPAccount, CCPCode)
        VALUES (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%%d/%%m/%%Y'), %s, %s, %s, %s)
        """
        cursor.execute(query, (nom, prenom, email, phone, nin, birth_date, wilaya, commune, ccp_account, ccp_code))
        conn.commit()  # enregestrer dans la base de donner 
        cursor.close()
        conn.close()
        return True
    else:
        return False


class PageOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

    
        background_path = r"v704-aew-25-neonbackground.jpg"
        img = Image(source=background_path, allow_stretch=True, keep_ratio=False)
        layout.add_widget(img)

        
        title = Label(
            text="My APK",
            font_size='40sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            pos_hint={"top": 1, "center_x": 0.5}
        )
        layout.add_widget(title)

       

        
        button_formulaire = Button(
            text="formulaire",
            font_size='24sp',
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color = (0.0, 0.0, 1.0, 1.0),

            color=(1, 1, 1, 1),
        )
        button_formulaire.bind(on_release=self.go_to_formulaire)
        layout.add_widget(button_formulaire)

        
        button_rechercher = Button(
            text="rechercher",
            font_size='20sp',
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.3, "center_y": 0.3},
            background_color = (0.0, 0.0, 1.0, 1.0),

            color=(1, 1, 1, 1)
        )
        button_rechercher.bind(on_release=self.go_to_rechercher)

        layout.add_widget(button_rechercher)

        button_parametre = Button(
            text="parametre",
            font_size='20sp',
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.7, "center_y": 0.3},
            background_color = (0.0, 0.0, 1.0, 1.0),

            color=(1, 1, 1, 1)
        )
        layout.add_widget(button_parametre)

        
      
        exit_button = Button(
            text="Quiter",
            font_size='20sp',
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            background_color = (0.0, 0.0, 1.0, 1.0),

            color=(1, 1, 1, 1)
        )
        exit_button.bind(on_release=self.exit_app)  #fonction exitapp
        layout.add_widget(exit_button)
        self.add_widget(layout)
    
    def exit_app(self, instance):
        App.get_running_app().stop()  # quiter apk



    def go_to_rechercher(self, instance):
        self.manager.current = "rechercher"  # fonction de butone recherch

     
    def go_to_formulaire(self, instance):
        self.manager.current = "formulaire"  # fonction de buton de formulaire
class PageRechercher(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# classe PageRechercher qui hérite de la classe Screen de Kivy. La classe Screen est utilisée avec ScreenManager pour créer des interfaces comportant plusieurs "pages" ou écrans dans une application.
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        
        background_path = r"téléchargement (1).jpeg"
        img = Image(source=background_path, allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(img)

        # widget de recher 
        self.search_input = TextInput(
            hint_text="wilaya",
            size_hint=(0.6, 0.1),
            pos_hint={"center_x": 0.5, "top": 0.9}
        )
        self.layout.add_widget(self.search_input)

        
        search_button = Button(
            text="rechercher",
            size_hint=(0.2, 0.1),
            pos_hint={"center_x": 0.8, "top": 0.9}
        )
        search_button.bind(on_release=self.perform_search)
        self.layout.add_widget(search_button)

        # table de recherch
        self.results_layout = GridLayout(
            cols=10,  # les colones egala de la table
            size_hint_y=None,
            spacing=10
        )
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))

        # ScrollView POUR AFICHER LE TABL
        self.scroll_view = ScrollView(
            size_hint=(1, 0.8),
            pos_hint={"center_x": 0.5, "top": 0.8}
        )
        self.scroll_view.add_widget(self.results_layout)
        self.layout.add_widget(self.scroll_view)

        # AFFICHER TOUS LA TABLE 
        self.perform_search(None)
            
        back_button = Button(
            text="Retour",
            size_hint=(0.2, 0.1),
            pos_hint={"center_x": 0.1, "top": 0.95},
            background_color = (0.0, 0.0, 1.0, 1.0),

        )
        back_button.bind(on_release=self.go_back) 
        self.layout.add_widget(back_button)
    def go_back(self, instance):
        self.manager.current = "home"  # go to home 


    def perform_search(self, instance):
        search_term = self.search_input.text.strip()  # jib txt mn recherch 
        self.results_layout.clear_widgets()  # cler table avant de modifier 

        conn = connect_db()  # connecter au base de donner 
        if conn:
            cursor = conn.cursor()
            # bch tjib inof
            if search_term:
                query = "SELECT * FROM users WHERE Wilaya LIKE %s"
                params = (f"%{search_term}%",)
            else:
                query = "SELECT * FROM users"
                params = ()

            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            conn.close()

            
            headers = ["ID", "Nom", "Prénom", "AdresseMail", "NuméroDeTéléphone", "NIN", "DateDeNaissance", "Wilaya", "Commune", "CCPAccount"]
            for header in headers:
                self.results_layout.add_widget(Label(text=header, bold=True, size_hint_y=None, height=40))

            # afficher resultat de recherch 
            if results:
                for row in results:
                    for cell in row:
                        self.results_layout.add_widget(Label(text=str(cell), size_hint_y=None, height=40))
            else:
                self.results_layout.add_widget(Label(text="no donner", size_hint_y=None, height=40))
        else:
            self.results_layout.add_widget(Label(text="erreur de conixion", size_hint_y=None, height=40))


# page de formulaire 
class PageTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

       
        back_button = Button(
            text="Retour",
            size_hint=(0.2, 0.1),
            pos_hint={"center_x": 0.1, "top": 0.95},
            background_color = (0.0, 0.0, 1.0, 1.0),
        )
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

    def go_back(self, instance):
        self.manager.current = "home"  

        layout = BoxLayout(orientation="vertical")

        
        title_label = Label(text='Formulaire de location appartement', font_size=30, size_hint=(1, 0.1))
        layout.add_widget(title_label)

        
        subtitle_label = Label(
            text='Bienvenue ici sur notre apk pour vous inscrire à la location de maisons en Algérie',
            font_size=20,
            size_hint=(1, 0.15)
        )
        layout.add_widget(subtitle_label)

        
        self.fields = {}
        self.add_field(layout, "Nom", "Nom")
        self.add_field(layout, "Prénom", "Prénom")
        self.add_field(layout, "Adresse Mail", "Adresse Email")
        self.add_field(layout, "Numéro de téléphone", "Numéro de téléphone")
        self.add_field(layout, "NIN", "Numéro d'identification nationale")
        self.add_field(layout, "Date de naissance", "DD/MM/YYYY")
        self.add_spinner(layout, "Wilaya", wilayas)
        self.add_field(layout, "Commune", "Commune")
        self.add_spinner(layout, "Type d'appartement", ["F1", "F2", "F3", "F4"])

        optional_label = Label(
            text='Si vous souhaitez payer avec un compte CCP',
            font_size=20,
            size_hint=(1, 0.15)
        )
        layout.add_widget(optional_label)
        self.add_field(layout, "Numéro de compte CCP", "Numéro de compte CCP")
        self.add_field(layout, "Code CCP", "Code CCP")
        # les buuton 
        self.add_buttons(layout)
        self.add_widget(layout)
# pour ajouter les champ au intrface 
    def add_field(self, layout, field_name, hint_text):
        field_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=40)
        label = Label(text=field_name, size_hint_x=0.3)
        text_input = TextInput(hint_text=hint_text, size_hint_x=0.7)
        field_layout.add_widget(label)
        field_layout.add_widget(text_input)
        self.fields[field_name] = text_input
        layout.add_widget(field_layout)
# pour ajouter la list 
    def add_spinner(self, layout, field_name, values):
        spinner_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=40)
        label = Label(text=field_name, size_hint_x=0.3)
        spinner = Spinner(text="Choisir...", values=values, size_hint_x=0.7)
        spinner_layout.add_widget(label)
        spinner_layout.add_widget(spinner)
        self.fields[field_name] = spinner
        layout.add_widget(spinner_layout)
# pour ajouter les buttons
    def add_buttons(self, layout):
        buttons_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
        submit_button = Button(text="Demander un appartement")
        submit_button.bind(on_release=self.submit_form)
        buttons_layout.add_widget(submit_button)

        reset_button = Button(text="Réinitialiser")
        reset_button.bind(on_release=self.reset_form)
        buttons_layout.add_widget(reset_button)

        layout.add_widget(buttons_layout)
# la verfication des champs 
    def submit_form(self, instance):
        errors = []
        data = {field: widget.text.strip() for field, widget in self.fields.items()}
#isalpha verfie si chain de char contien que des lettre 
        
        if not data["Nom"].isalpha():
            errors.append("Le champ 'Nom' doit contenir uniquement des lettres.")

        
        if not data["Prénom"].isalpha():
            errors.append("Le champ 'Prénom' doit contenir uniquement des lettres.")

    # re.fullmatch(expRGL,lachain qui on verfie )
        if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", data["Adresse Mail"]):
            errors.append("Le champ 'Adresse Mail' doit contenir un email valide se terminant par @gmail.com.")

        # isdigit que des chifre 
        if not data["Numéro de téléphone"].isdigit():
            errors.append("Le champ 'Numéro de téléphone' doit contenir uniquement des chiffres.")

        
        if not data["NIN"].isdigit():
            errors.append("Le champ 'NIN' doit contenir uniquement des chiffres.")

        
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", data["Date de naissance"]):
            errors.append("Le champ 'Date de naissance' doit respecter le format DD/MM/YYYY.")

        # si il ya erreur 
        if errors:
            popup = Popup(
                title="Erreurs de validation",
                content=Label(text="\n".join(errors)),
                size_hint=(0.6, 0.6)
            )
            popup.open()
            return

        # ajouter les donnes au BD
        if insert_data(data["Nom"], data["Prénom"], data["Adresse Mail"], data["Numéro de téléphone"], 
                       data["NIN"], data["Date de naissance"], data["Wilaya"], data["Commune"], 
                       data["Numéro de compte CCP"], data["Code CCP"]):
            popup = Popup(
                title="Succès",
                content=Label(text="Les données ont été enregistrées avec succès !"),
                size_hint=(0.6, 0.6)
            )
            popup.open()

    def reset_form(self, instance):
        for widget in self.fields.values():
            widget.text = ""



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PageOne(name="home"))
        sm.add_widget(PageRechercher(name="rechercher"))
        sm.add_widget(PageTwo(name="formulaire"))
        return sm


if __name__ == "__main__":
    MyApp().run()
