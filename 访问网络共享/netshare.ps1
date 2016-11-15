
$Device = [Environment]::GetLogicalDrives()|Where-Object{$_ -eq "M:\"}

$code = @()

if($Device)
{
    net use M: /del
}else
{
    $array = 0..255

    foreach($ip1 in $array)
    {
         "net use M: \\202.115.52.$ip1\3dworkshare" | Out-File .\$ip1.ps1
    }
 #  Invoke-Expression $code[$ip]
    foreach($ip2 in $array)
    {
        Start-Job -FilePath .\$ip2.ps1 | Wait-Job -Timeout 3
    }
    

}