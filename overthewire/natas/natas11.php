<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_decrypt($in) {
	$key = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=');
	$text = $in;
	$outText = '';

	for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^$key[$i % strlen($key)];
	}

	return $outText;
}

$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
	$key = 'qw8J';
	$text = $in;
	$outText = '';

	for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^$key[$i % strlen($key)];
	}

	return $outText;
}

echo base64_encode(xor_encrypt(json_encode($data)));
?>