---
title: "Modify Derived Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Derived_Part_Example_VB.htm"
---

# Modify Derived Part Example (VBA)

This example shows how to insert and modify a derived part.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the part documents to open and insert exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Inserts a derived part in the part document
'    opened in step 1.
' 3. Changes some parameters of the derived part feature.
' 4. Examine the Immediate window.
'
' NOTE: Because both part documents are used elsewhere,
' do not save any changes.
'-----------------------------------------------
```

```
Option Explicit
```

```
Function TestImportPlane(feat As Feature, doc As ModelDoc2, comp As Component2) As Boolean
    Dim featData As SldWorks.DerivedPartFeatureData
    Dim startVal As Boolean
    Dim boolstatus As Boolean
```

```
    Set featData = feat.GetDefinition
    startVal = featData.ImportPlane
    Debug.Print "Import planes with derived part? " & startVal
    featData.ImportPlane = True
    Debug.Print "Modified import planes with derived part? " & featData.ImportPlane
    boolstatus = feat.ModifyDefinition(featData, doc, comp)
    Set featData = Nothing
End Function
```

```
Function TestImportAbsorbedSketches(feat As Feature, doc As ModelDoc2, comp As Component2) As Boolean
    Dim featData As SldWorks.DerivedPartFeatureData
    Dim startVal As Boolean
    Dim boolstatus As Boolean
```

```
    Set featData = feat.GetDefinition
    startVal = featData.ImportAbsorbedSketches
    Debug.Print "Import absorbed sketches with derived part? " & startVal
    featData.ImportAbsorbedSketches = True
    Debug.Print "Modified import absorbed sketches with derived part? " & featData.ImportAbsorbedSketches
    boolstatus = feat.ModifyDefinition(featData, doc, comp)
    Set featData = Nothing
End Function
```

```
Function TestImportUnAbsorbedSketches(feat As Feature, doc As ModelDoc2, comp As Component2) As Boolean
    Dim featData As SldWorks.DerivedPartFeatureData
    Dim startVal As Boolean
    Dim boolstatus As Boolean

    Set featData = feat.GetDefinition
    startVal = featData.ImportUnAbsorbedSketches
    Debug.Print "Import unabsorbed sketches with derived part? " & startVal
    featData.ImportUnAbsorbedSketches = True
    Debug.Print "Modified import unabsorbed sketches with derived part? " & featData.ImportUnAbsorbedSketches
    boolstatus = feat.ModifyDefinition(featData, doc, comp)
    Set featData = Nothing
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swComp As SldWorks.Component2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDerivedFeat As SldWorks.Feature
    Dim swFeat As SldWorks.Feature
    Dim swDerivedData As SldWorks.DerivedPartFeatureData
    Dim bRet As Boolean
    Dim fileName As String
    Dim derivedFileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks

    'Open part, insert another part, and select the derived part feature
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\holecube.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    derivedFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swPart = swModel
    Set swFeat = swPart.InsertPart3(derivedFileName, swInsertPartOptions_e.swInsertPartImportSolids, "Default")
    swModel.ClearSelection2 True
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("box", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
```

```
    'Get the selected derived part feature
    Set swSelMgr = swModel.SelectionManager
    Set swDerivedFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
    Debug.Print "Name of derived part feature = " & swDerivedFeat.Name
```

```
    Debug.Print ""
    'Get and modify import planes with derived part
    bRet = TestImportPlane(swDerivedFeat, swModel, swComp)
    Debug.Print ""
    'Get and modify import absorbed sketches with derived part
    bRet = TestImportAbsorbedSketches(swDerivedFeat, swModel, swComp)
    Debug.Print ""
    'Get and modify import unabsorbed sketches with derived part
    bRet = TestImportUnAbsorbedSketches(swDerivedFeat, swModel, swComp)
```

```
    Debug.Print ""
    Set swDerivedData = swDerivedFeat.GetDefinition
    Debug.Print "Derived file's path and name = " & swDerivedData.PathName
```

```
End Sub
```
