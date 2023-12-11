// Ouvrir le premier onglet au chargement de la page
document.addEventListener('DOMContentLoaded', function () {
    // Redirection 
    if (!(window.location.href.includes("#"))) {
        document.location.href = "#tabAPropos";
    }
});
