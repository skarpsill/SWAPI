---
title: "Get Mate Reference Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mate_Reference_Properties_Example_VB.htm"
---

# Get Mate Reference Properties Example (VBA)

This example shows how to get mate reference properties.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a mate reference.
' 3. Gets properties of the mate reference.
' 4. Examine the FeatureManager design tree and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swMateReference As SldWorks.MateReference
    Dim swFeature As SldWorks.Feature
    Dim mateRefObj As Object
    Dim mateRefEntityType As Long
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swPlane As SldWorks.Entity
    Dim swFeatureMgr As SldWorks.FeatureManager
    Dim strMateReferencename As String
    Dim nCount As Long
    Dim refEntType As Long
    Dim mateRefAlignment As Long
    Dim boolstatus As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Insert mate reference
    boolstatus = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swPlane = swSelMgr.GetSelectedObject6(1, -1)
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 8.35786916030656E-03, 4.29540237419701E-03, 0, True, 2, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.InsertMateReference2("Default", Nothing, 0, 1, False, Nothing, 0, 2, False, Nothing, 0, 0)
    swModel.ClearSelection2 True
```

```
    boolstatus = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swMateReference = swFeature.GetSpecificFeature2
    swModel.ClearSelection2 True
```

```
    ' Get the name of the mate reference
    strMateReferencename = swMateReference.Name
    Debug.Print "Name of mate reference = " & strMateReferencename
```

```
    nCount = swMateReference.ReferenceEntityCount
    Debug.Print "Number of mate reference entities = " & nCount
```

```
    refEntType = swMateReference.ReferenceType(0)
    Debug.Print "Mating type of primary mate entity is " & refEntType
```

```
    mateRefAlignment = swMateReference.ReferenceAlignment(0)
    Debug.Print "Alignment of primary mate entity = " & mateRefAlignment
```

```
    ' Get the  mate reference entity in the mate reference
    Set mateRefObj = swMateReference.ReferenceEntity2(0)
```

```
    ' Get the mate reference entity type
    mateRefEntityType = swMateReference.ReferenceEntityType(0)
    Debug.Print "Entity type of primary mate entity = " & mateRefEntityType
```

```
    ' QueryInterface the returned object as a face, if a face
    If mateRefEntityType = swSelectType_e.swSelFACES Then
        Dim mateRefFace As SldWorks.Face2
        Set mateRefFace = mateRefObj
        Debug.Print "Primary mate entity is a face with area = " & mateRefFace.GetArea
    End If
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
