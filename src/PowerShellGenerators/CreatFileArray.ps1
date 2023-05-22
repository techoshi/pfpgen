$folderPath = "C:\Users\joser\iCloudDrive\Bear Bears\Male\Hats"

# Get all PNG files in the specified folder
$pngFiles = Get-ChildItem -Path $folderPath -Filter *.png

# Create an array to store the objects
$jsonArray = @()

# Iterate over each PNG file
foreach ($file in $pngFiles) {
    # Create a hashtable representing the object
    $object = @{
        "name" = $file.BaseName
        "count" = 100
    }

    # Add the object to the JSON array
    $jsonArray += $object
}

# Convert the array to JSON
$jsonString = $jsonArray | ConvertTo-Json

# Output the JSON string
$jsonString
