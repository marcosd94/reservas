% En el sistema se cuentan con 3 roles, para eliminar un articulo se debe ser administrador o gestor y el articulo debe estar libre.
% Para eliminar un funcionario deber ser administrador
% Para reservar un articulo el articulo debe estar libre
% Para cargar un funcionario el codigo usuario siempre tiene que estar libre

administrador(mperalta).
gestor(jparedes).
reservas(pmarmol).

existe_usuario(Usuario):-  administrador(Usuario); gestor(Usuario);  reservas(Usuario).

articulo_activo(epson).
articulo_activo(notebook).
articulo_activo(impresora).
articulo_activo(notebook2).
articulo_activo(impresora2).

articulo_inactivo(impresora3).
articulo_inactivo(impresora4).

reservado(epson).
reservado(notebook).
reservado(impresora).

libre(notebook2).
libre(impresora2).
libre(impresora3).
libre(impresora4).

eliminar_articulo(Usuario, Articulo) :- (administrador(Usuario); gestor(Usuario)), libre(Articulo), articulo_activo(Articulo).
eliminar_funcionario(Usuario) :- administrador(Usuario).
reservar_articulo(Usuario, Articulo) :- (administrador(Usuario); gestor(Usuario); reservas(Usuario)), libre(Articulo), articulo_activo(Articulo).


cargar_funcionario(Usuario) :- not(existe_usuario(Usuario)).
