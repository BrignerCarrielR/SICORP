let partimonio = document.getElementById('id_patrimonio')
let apalancamiento = document.getElementById('id_apalancamiento')

partimonio.addEventListener("change", function() {
    let activo = Number(document.getElementById('id_activo').value)
    let partimonio = Number(document.getElementById('id_patrimonio').value)
    apalancamiento.value=activo/partimonio
});

