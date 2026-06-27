---
title: "Copy Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_Example_VB.htm"
---

# Copy Document Example (VBA)

This example shows how to copy a document.

```
'--------------------------------------
' Preconditions:
' 1. Verify that the specified file to copy exists.
' 2. Verify that c:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Copies C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt
'    to c:\temp\cstick.slprt. If c:\temp\cstick.sldprt already exists, the file is
'    overwritten.
' 2. Examine the Immediate window and c:\temp.
'---------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim fileName
Dim retVal As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
    retVal = swApp.CopyDocument(fileName, "c:\temp\cstick.sldprt", "", "", swMoveCopyOptionsOverwriteExistingDocs)
    Debug.Print "Status of copy (0 = success): " & retVal
```

```
End Sub
```
