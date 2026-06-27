---
title: "Get BOM Balloon Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BOM_Balloon_Properties_Example_VBNET.htm"
---

# Get BOM Balloon Properties Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swNote As Note
        Dim swAnnotation As Annotation
        Dim attachedEntityArray() As Object
        Dim attachedEntityTypeArray() As Integer
        Dim swEntity As Entity
        Dim swComponent As Component2
        Dim swComponentModel As ModelDoc2
        Dim swBomTableAnnotation As BomTableAnnotation
        Dim swBomBalloonParams As BalloonOptions
        Dim i As Integer
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open assembly, create BOM table, and select BOM balloon
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swBomTableAnnotation = swModelDocExt.InsertBomTable3("C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\bom-standard.sldbomtbt", 618, 568, swBomType_e.swBomType_TopLevelOnly, "", False, swNumberingType_e.swNumberingType_None, False)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0139294427590926, 0.059464184169542, 0.0082768338148469, False, 0, Nothing, 0)
        swBomBalloonParams = swModelDocExt.CreateBalloonOptions()
        swBomBalloonParams.Style = swBalloonStyle_e.swBS_SplitCirc
        swBomBalloonParams.Size = swBalloonFit_e.swBF_Tightest
        swNote = swModelDocExt.InsertBOMBalloon2(swBomBalloonParams)
        status = swModelDocExt.SelectByID2("DetailItem2@Annotations", "NOTE", 0.00431152692774954, 0.0699703491909496, 0.0033561420724473, False, 0, Nothing, 0)

        'Get and set balloon properties
        swSelectionMgr = swModel.SelectionManager
        swNote = swSelectionMgr.GetSelectedObject6(1, -1)
        swAnnotation = swNote.GetAnnotation
        attachedEntityArray = swAnnotation.GetAttachedEntities2
        attachedEntityTypeArray = swAnnotation.GetAttachedEntityTypes
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  Name = " & swAnnotation.GetName)
        swNote.SetBomBalloonText(swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "ABC", swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "EFG")
        Debug.Print("    Upper text = " & swNote.GetBomBalloonText(True) & " [" & swNote.GetBomBalloonTextStyle(True) & "]")
        Debug.Print("    Lower text = " & swNote.GetBomBalloonText(False) & " [" & swNote.GetBomBalloonTextStyle(False) & "]")
        Debug.Print("    Balloon fit = " & swNote.GetBalloonSize)
        Debug.Print("    Balloon style = " & swNote.GetBalloonStyle)
	Debug.Print("    Balloon padding = " & swNote.GetBalloonPadding)
        Debug.Print("    Is stacked? " & swNote.IsStackedBalloon)
        Debug.Print("    Is stacked master? " & swNote.IsStackedBalloonMaster)
        For i = 0 To UBound(attachedEntityArray)
            Debug.Print("    Attached entity type = " & attachedEntityTypeArray(i))
            If (Not IsNothing(attachedEntityTypeArray)) Then
                swEntity = attachedEntityArray(i)
                swComponent = swEntity.GetComponent
                swComponentModel = swComponent.GetModelDoc
                Debug.Print("    Attached entity = " & swComponent.GetPathName & " <" & swComponent.ReferencedConfiguration & ">" & " --> " & swComponentModel.GetPathName)
            End If
        Next i
```

```
	swModel.ViewZoomtoFit2

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
