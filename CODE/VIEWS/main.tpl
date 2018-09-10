<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<meta name="viewport" content="width=device-width initial-scale=1.0" />

<link href="Boot/Bootstrap3/css/bootstrap.min.css" rel="stylesheet" media="screen" />

<link href="Boot/Bootstrap3/css/estilo.css" rel="stylesheet" media="screen" />

<title>Direcionador de Tela</title>
</head>
<body>
	<div class="container">
		<div class="row">
			<form class="form-horizontal" action="direciona" name="direciona" method="post">
				<div class="form-group">
					<div class="col-xs-12">
						<label for="cargo">Selecione o Cargo:</label>
					</div>
					<div class="col-xs-6">
						<select class="form-control" id="cargo" name="cargo" size="1">
							<option value="atendente">Atendente</option>
							<option value="infermeiro">Enfermeiro</option>
							<option value="Medico">Medico</option>
						</select>
					</div>
					<div class="col-xs-6">
						<input class="form-control" type="text" id="id" name="id" value="Numero do Documento" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
				</div>
				<div class="form-group">
					<div class="col-xs-12">
						<button class="form-control btn btn-block btn-primary" id="direciona" name="encaminha" type="submit"/>Entrar		
					</div>
				</div>
			</form>
		</div>	
	</div>
	<script src="Boot/Bootstrap3/js/jquery-1.11.1.min.js"></script>
   	<script src="Boot/Bootstrap3/js/bootstrap.min.js"></script>
	<script src="Boot/Bootstrap3/js/main.js"></script>
</body>
</html>



