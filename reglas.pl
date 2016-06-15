% En el sistema se cuentan con 3 roles, para eliminar un articulo se debe ser administrador o gestor.
% Para eliminar un funcionario deber ser administrador

administrador(mperalta).
gestor(jparedes).
reservas(pmarmol).

eliminar_articulo(Usuario) :- administrador(Usuario); gestor(Usuario).
eliminar_funcionario(Usuario) :- administrador(Usuario).
reservar_articulo(Usuario) :- administrador(Usuario); gestor(Usuario); reservas(Usuario).
