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
			<form class="form-horizontal" action="procura_paciente" name="procura" method="post">
				<div class="form-group">
					<div class="col-xs-12">
						<label for="cpf">CPF do Paciente:</label>
					</div>
					<div class="col-xs-8">
						<input class="form-control" type="text" id="busca_cpf" name="busca_cpf" value="{{busca}}"" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-4">
						<button class="form-control btn btn-block btn-primary" id="proc_paciente" name="proc_paciente" type="submit"/>Procurar
					</div>
				</div>	
			</form>
			<form class="form-horizontal" id="dados" action="novo_paciente" name="cadastra" method="post">
				<div class="form-group">
					<div class="col-xs-8">
						<label for="nome">Nome do Pacinete:</label>
					</div>
					<div class="col-xs-4">
						<label for="idade">Idade do Pacinete:</label>
					</div>
					<div class="col-xs-8">
						<input class="form-control" type="text" id="nome" name="nome" value="{{nome}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-4">
						<input class="form-control" type="text" id="idade" name="idade" value="{{idade}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
				</div>
				<div class="form-group">
					<div class="col-xs-6">
						<label for="rg">RG do Pacinete:</label>
					</div>
					<div class="col-xs-6">
						<label for="cpf">CPF do Pacinete:</label>
					</div>
					<div class="col-xs-6">
						<input class="form-control" type="text" id="rg" name="rg" value="{{rg}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-6">
						<input class="form-control" type="text" id="cpf" name="cpf" value="{{cpf}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
				</div>
				<div class="form-group">
					<div class="col-xs-4">
						<label for="pais">Pais:</label>
					</div>
					<div class="col-xs-4">
						<label for="estado">Estado:</label>
					</div>
					<div class="col-xs-4">
						<label for="cidade">Cidade:</label>
					</div>
					<div class="col-xs-4">
						<input class="form-control" type="text" id="pais" name="pais" value="{{pais}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-4">
						<input class="form-control" type="text" id="estado" name="estado" value="{{estado}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-4">
						<input class="form-control" type="text" id="cidade" name="cidade" value="{{cidade}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
				</div>
				<div class="form-group">
					<div class="col-xs-5">
						<label for="bairro">Bairro:</label>
					</div>
					<div class="col-xs-5">
						<label for="rua">Rua:</label>
					</div>
					<div class="col-xs-2">
						<label for="numero">Numero:</label>
					</div>
					<div class="col-xs-5">
						<input class="form-control" type="text" id="bairro" name="bairro" value="{{bairro}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-5">
						<input class="form-control" type="text" id="rua" name="rua" value="{{rua}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-2">
						<input class="form-control" type="text" id="numero" name="numero" value="{{numero}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>	
				</div>
				<div class="form-group">
					<div class="col-xs-12">
						<label for="cep">CEP:</label>
					</div>
					<div class="col-xs-6">
						<input class="form-control" type="text" id="cep" name="cep" value="{{cep}}" onclick="this.setSelectionRange(0, this.value.length)"/>
					</div>
					<div class="col-xs-2">
						<button class="form-control btn btn-block btn-primary" id="cadastra" name="cadastra" type="submit"/>Novo Paciente	
					</div>	
					<div class="col-xs-2">
						<button class="form-control btn btn-block btn-primary" form="dados" formaction="atualiza_paciente" id="atualiza" name="atualiza" type="submit"/>Atualiza Paciente	
					</div>
					<div class="col-xs-2">
						<button class="form-control btn btn-block btn-primary" form="dados" formaction="encaminha_paciente" id="encaminha" name="encaminha" type="submit"/>Encaminhar	
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



