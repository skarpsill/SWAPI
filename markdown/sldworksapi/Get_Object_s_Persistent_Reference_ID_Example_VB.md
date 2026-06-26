---
title: "Get Object's Persistent Reference ID Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Object_s_Persistent_Reference_ID_Example_VB.htm"
---

# Get Object's Persistent Reference ID Example (VBA)

This example shows how to get an object's persistent reference IDs.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part that contains an Extrude1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the persistent reference ID of the Extrude1 feature
'    after after releasing its object, after rebuilding the part,
'    after closing and opening the part document.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim docext As SldWorks.ModelDocExtension
Dim pathname As String
Dim filetype As Long
Dim errors As Long
Dim warnings As Long
Dim options As Long
Dim obj As Object
Dim reference As Variant
Dim index As Integer
Dim boolstatus As Boolean
Dim errorCode As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Get the document
    Set Part = swApp.ActiveDoc
    Set docext = Part.Extension
```

```
    'Get the object
    boolstatus = Part.Extension.SelectByID2("Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set obj = Part.SelectionManager.GetSelectedObject5(1)
```

```
    'Get the object's reference id
    reference = docext.GetPersistReference3(obj)
```

```
    'After releasing the object with the part remaining available
    Set obj = Nothing
    Set obj = docext.GetObjectByPersistReference3(reference, errorCode)
    Debug.Print "Get object by persistent reference ID after releasing object: " & errorCode
```

```
    'After rebuilding the part
    Set obj = Nothing
    Call Part.Rebuild(swForceRebuildAll)
    Set obj = docext.GetObjectByPersistReference3(reference, errorCode)
    Debug.Print "Get object by persistent reference ID after rebuilding part: " & errorCode
```

```
    'After closing and opening the part
    Set obj = Nothing
    pathname = Part.GetPathName
    swApp.CloseDoc pathname
    Set Part = Nothing
    Set docext = Nothing
    Set Part = swApp.GetOpenDocumentByName(pathname)
    Set Part = swApp.OpenDoc6(pathname, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set docext = Part.Extension
    Set obj = docext.GetObjectByPersistReference3(reference, errorCode)
    Debug.Print "Get object by persistent reference ID after closing and opening part: " & errorCode
```

```
End Sub
```
