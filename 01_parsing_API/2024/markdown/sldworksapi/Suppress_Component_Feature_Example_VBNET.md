---
title: "Suppress Component Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Component_Feature_Example_VBNET.htm"
---

# Suppress Component Feature Example (VB.NET)

This example shows how to suppress the selected component feature.

```
'------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component feature in the FeatureManager
'    design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Suppresses the selected component feature.
' 2. Prints the names of the assembly and the suppressed
'    component feature to the Immediate window.
' 3. Examine the Immediate window.
'
' NOTE: Editing a component requires that geometry on
' the component be selected. However, not
' all features are associated with geometry.
' Therefore, it is necessary to select the component
' before attempting to edit the component.
'------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swAssy As AssemblyDoc
        Dim swEditModel As ModelDoc2
        Dim swEditPart As PartDoc
        Dim swEditAssy As AssemblyDoc
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swComp As Component2
        Dim featName As String
        Dim status As Integer
        Dim info As Integer
        Dim retVal As Boolean

        swModel = swApp.ActiveDoc
        swAssy = swModel
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1) : Debug.Assert(Not swFeat Is Nothing)
        swComp = swSelMgr.GetSelectedObjectsComponent2(1) : Debug.Assert(Not swComp Is Nothing)

        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("    " & swFeat.Name & " <" & swFeat.GetTypeName & ">")
        Debug.Print("")

        featName = swFeat.Name
        retVal = swComp.Select2(False, 0) : Debug.Assert(retVal)
        status = swAssy.EditPart2(True, False, info) : Debug.Assert(swEditPartCommandStatus_e.swEditPartSuccessful = status)
        swEditModel = swAssy.GetEditTarget

        Select Case swEditModel.GetType
            Case swDocumentTypes_e.swDocPART
                swEditPart = swEditModel
                swFeat = swEditPart.FeatureByName(featName) : Debug.Assert(Not swFeat Is Nothing)
                retVal = swFeat.Select2(False, 0) : Debug.Assert(retVal)
            Case swDocumentTypes_e.swDocASSEMBLY
                swEditAssy = swEditModel
                swFeat = swEditAssy.FeatureByName(featName) : Debug.Assert(Not swFeat Is Nothing)
                retVal = swFeat.Select2(False, 0) : Debug.Assert(retVal)
            Case Else
                Debug.Assert(False)
        End Select

        ' Suppress the selected feature;
        retVal = swEditModel.EditSuppress2 : Debug.Assert(retVal)
        swAssy.EditAssembly()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
