class Translator:
    def __init__(self):
        self.translations = {
            "es": {
                "menu_settings": "Configuración",
                "menu_exit": "Salir",
                "menu_move": "Mover ventana",
                "dialog_title": "Configuración del Reloj",
                "category_background": "Fondo",
                "category_border": "Borde",
                "category_display": "Visualización",
                "category_language":"Idioma",
                "category_help": "Ayuda",
                "bg_change_color": "Cambiar color de fondo",
                "bg_opacity": "Opacidad del fondo (%)",
                "bg_text_color": "Cambiar color del texto",
                "border_change_color": "Cambiar color del borde",
                "border_thickness": "Grosor del borde",
                "border_radius": "Radio de bordes",
                "display_seconds": "Mostrar segundos",
                "display_date": "Mostrar fecha",
                "date_format": "Formato de fecha:",
                "font_label": "Fuente:",
                "font_size": "Tamaño de fuente:",
                "window_size": "<b>Tamaño de ventana</b>",
                "width_label": "Ancho",
                "height_label": "Alto",
                "help_title": "<h2>Reloj Flotante</h2>",
                "help_description": "<ul><li>Un simple reloj para configurar un atajo de teclado y que aparezca en pantalla. Usado en Fedora KDE</li></ul>",
                "help_usage": """<h2>Instrucciones de uso:</h2>
                                <ul><li><b>Clic izquierdo:</b> Mantén pulsado para mover el reloj por la pantalla.</li>
                                <li><b>Clic central (rueda del ratón):</b> Mantén pulsado para redimensionar el reloj.</li></ul>"""
            },
            "en": {
                "menu_settings": "Settings",
                "menu_exit": "Exit",
                "menu_move": "Move window",
                "dialog_title": "Clock Configuration",
                "category_background": "Background",
                "category_border": "Border",
                "category_display": "Display",
                "category_language":"Language",
                "category_help": "Help",
                "bg_change_color": "Change background color",
                "bg_opacity": "Background opacity (%)",
                "bg_text_color": "Change text color",
                "border_change_color": "Change border color",
                "border_thickness": "Border thickness",
                "border_radius": "Border radius",
                "display_seconds": "Show seconds",
                "display_date": "Show date",
                "date_format": "Date format:",
                "font_label": "Font:",
                "font_size": "Font size:",
                "window_size": "<b>Window size</b>",
                "width_label": "Width",
                "height_label": "Height",
                "help_title": "<h2>Floating Clock</h2>",
                "help_description": "<ul><li>A simple clock to configure a keyboard shortcut and appear on screen. Used in Fedora KDE</li></ul>",
                "help_usage": """<h2><b>Usage instructions:</b></h2>
                                <ul><li><b>Left click:</b> Hold and drag to move the clock.</li>
                                <li><b>Middle click (wheel):</b> Hold and drag to resize the clock.</li></ul>"""
            }
        }
    
    def tr(self, key):
        return self.translations[self.language].get(key, key)
    
    def get_category(self, key):
        """Obtiene traducción específica para categorías"""
        category_key = f"category_{key}"
        return self.translations[self.language].get(category_key, key)
    
    def get_setting(self, section, key):
        """Obtiene traducción para ajustes específicos"""
        setting_key = f"{section}_{key}"
        return self.translations[self.language].get(setting_key, key)
    
    def set_language(self, language):
        self.language = language
        
    def get_language(self):
        return self.language