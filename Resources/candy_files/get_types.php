<?php

$types = [];
$c=0;
for($i=1;$i<=5;$i++){
    $data = json_decode(file_get_contents("candy_{$i}.json"),true);
    foreach($data as $candy){
        if(!in_array($candy['type'],$types)){
            $types["{$c}"] = $candy['type'];
            $c++;
        }
    }
}

//$types = array_flip($types);
$i=0;
echo"[\n";
foreach($types as $type){
    echo"\t{\"id\":\"{$i}\",\"type\":\"{$type}\"},\n";
    $i++;
}