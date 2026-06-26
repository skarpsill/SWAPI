---
title: "Insert Mate Load Reference Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Mate_Load_Reference_Example_VBNET.htm"
---

# Insert Mate Load Reference Example (VB.NET)

This example shows how to insert a mate load reference.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Gets the mate where to add a load reference.
' 3. Selects a supplemental face for the load reference.
' 4. Inserts a mate load reference.
' 5. Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do
' not save changes.
'-------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssemblyDoc As AssemblyDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swMate As Mate2
        Dim swMateLoadRef As MateLoadReference
        Dim swFeat As Feature
        Dim swComponent As Component2
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean

        'Open the assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssemblyDoc = swModel
        swSelMgr = swModel.SelectionManager
        swModelDocExt = swModel.Extension

        'Get the mate where to add the load reference
        status = swModelDocExt.SelectByID2("Concentric4", "MATE", 0, 0, 0, False, 0, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, 0)
        swMate = swFeat.GetSpecificFeature2

        'Insert the load reference using the selected mate and supplemental face
        status = swModelDocExt.SelectByID2("", "FACE", 0.087090587167495, -0.00524931403344908, 0.00483048001655106, True, 0, Nothing, 0)
        swMateLoadRef = swAssemblyDoc.InsertLoadReference(swMate)
        Debug.Print("Name of load reference added to " & swFeat.Name & " mate = " & swMateLoadRef.Name)
        Debug.Print("Number of supplemental faces of the mate load reference for Component1 = " & swMateLoadRef.GetFacesCount(0))
        swComponent = swMateLoadRef.Component(0)
        Debug.Print("Name of Component1 = " & swComponent.Name2)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
