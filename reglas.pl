% En el sistema se cuentan con 3 roles, para eliminar un articulo se debe ser administrador o gestor.
% Para eliminar un funcionario deber ser administrador

administrador(mperalta).
gestor(jparedes).
reservas(pmarmol).

eliminar_articulo(X) :- administrador(X); gestor(X).
eliminar_funcionario(X) :- administrador(X).
reservar_articulo(X) :- administrador(X); gestor(X); reservas(X).
