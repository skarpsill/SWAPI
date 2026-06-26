---
title: "Get BOM Balloon Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BOM_Balloon_Properties_Example_VB.htm"
---

# Get BOM Balloon Properties Example (VBA)

This example shows how to get the properties of a BOM balloon.

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Inserts a BOM table.
' 3. Inserts a BOM balloon.
' 4. Gets and sets the BOM balloon's properties.
' 5. Examine the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.Note
Dim swAnnotation As SldWorks.Annotation
Dim attachedEntityArray As Variant
Dim attachedEntityTypeArray As Variant
Dim swEntity As SldWorks.Entity
Dim swComponent As SldWorks.Component2
Dim swComponentModel As SldWorks.ModelDoc2
Dim swBomTableAnnotation As SldWorks.BomTableAnnotation
Dim swBomBalloonParams As SldWorks.BalloonOptions
Dim i As Long
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly, create BOM table, and select BOM balloon
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swBomTableAnnotation = swModelDocExt.InsertBomTable3("C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\bom-standard.sldbomtbt", 618, 568, swBomType_e.swBomType_TopLevelOnly, "", False, swNumberingType_e.swNumberingType_None, False)
    status = swModelDocExt.SelectByID2("", "FACE", 1.39294427590926E-02, 0.059464184169542, 8.2768338148469E-03, False, 0, Nothing, 0)
    Set swBomBalloonParams = swModelDocExt.CreateBalloonOptions()
    swBomBalloonParams.Style = swBalloonStyle_e.swBS_SplitCirc
    swBomBalloonParams.Size = swBalloonFit_e.swBF_Tightest
    Set swNote = swModelDocExt.InsertBOMBalloon2(swBomBalloonParams)
    status = swModelDocExt.SelectByID2("DetailItem2@Annotations", "NOTE", 4.31152692774954E-03, 6.99703491909496E-02, 3.3561420724473E-03, False, 0, Nothing, 0)
```

```
    'Get and set BOM balloon properties
    Set swSelectionMgr = swModel.SelectionManager
    Set swNote = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swAnnotation = swNote.GetAnnotation
    attachedEntityArray = swAnnotation.GetAttachedEntities2
    attachedEntityTypeArray = swAnnotation.GetAttachedEntityTypes
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Name = " & swAnnotation.GetName
    swNote.SetBomBalloonText swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "ABC", swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "EFG"
    Debug.Print "    Upper text  = " & swNote.GetBomBalloonText(True) & " [" & swNote.GetBomBalloonTextStyle(True) & "]"
    Debug.Print "    Lower text  = " & swNote.GetBomBalloonText(False) & " [" & swNote.GetBomBalloonTextStyle(False) & "]"
    Debug.Print "    Balloon fit = " & swNote.GetBalloonSize
    Debug.Print "    Balloon style = " & swNote.GetBalloonStyle
    Debug.Print "    Balloon padding = " & swNote.GetBalloonPadding
    Debug.Print "    Is stacked? " & swNote.IsStackedBalloon
    Debug.Print "    Is stacked master? " & swNote.IsStackedBalloonMaster
    For i = 0 To UBound(attachedEntityArray)
        Debug.Print "    Attached entity type = " & attachedEntityTypeArray(i)
        If swSelNOTHING <> attachedEntityTypeArray(i) Then
            Set swEntity = attachedEntityArray(i)
            Set swComponent = swEntity.GetComponent
            Set swComponentModel = swComponent.GetModelDoc
            Debug.Print "    Attached entity = " & swComponent.GetPathName & " <" & swComponent.ReferencedConfiguration & ">" & " --> " & swComponentModel.GetPathName
        End If
    Next i
```

```
    swModel.ViewZoomtofit2

End Sub
```
