.\.venv\Scripts\activate

cd -Path "C:\Users\alpdi\programming\shorty\backend"
$path = Get-Location
Write-Output $path
Start-Process "waitress-serve" -ArgumentList "app:app"

Start-Process "python" -ArgumentList "vol.py"

cd -Path "C:\Users\alpdi\programming\shorty\frontend"

npm start 

