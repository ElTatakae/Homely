document.addEventListener('DOMContentLoaded', (event) => {
    // Seleccionar el elemento
    const serviceCountDiv = document.getElementById('photo-count');

    // Contar los servicios mostrados
    const displayedServices = document.querySelectorAll('.card.h-100').length;

    // Actualizar el texto en el elemento
    serviceCountDiv.textContent = `Mostrando ${displayedServices} servicios.`;
});