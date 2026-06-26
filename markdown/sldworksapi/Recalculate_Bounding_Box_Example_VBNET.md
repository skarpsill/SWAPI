---
title: "Recalculate Bounding Box Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Recalculate_Bounding_Box_Example_VBNET.htm"
---

# Recalculate Bounding Box Example (VB.NET)

This example shows how to recalculate the bounding box of an assembly.

```
'-----------------------------------------
' Preconditions:
' 1. Specified assembly document exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens assembly document.
' 2. Gets the bounding box for the assembly.
' 3. Prints the lower- and upper-diagonal corner points
'    of the bounding box to the Immediate window.
' 4. Modifies a dimension in a component in the assembly.
' 5. Updates the bounding box.
' 6. Prints the lower- and upper-diagonal corner points
'    of the bounding box to the Immediate window.
' 7. Examine the values printed to the Immediate window
'    to verify that the bounding box was updated.
'
' NOTE: Because this assembly is used elsewhere,
' do not save any changes when closing it.
'-------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swAssy As AssemblyDoc
    Dim swModelDocExt As ModelDocExtension
    Dim swDimension As Dimension
    Dim fileName As String
    Dim errors As Integer
    Dim warnings As Integer
    Dim status As Boolean

    Sub ProcessAssyBox(ByVal swApp As SldWorks, ByVal swAssy As AssemblyDoc)
        Dim vBox As Object
        vBox = swAssy.GetBox(0)
        Debug.Print("  Min = (" & vBox(0) * 1000.0# & ", " & vBox(1) * 1000.0# & ", " & vBox(2) * 1000.0# & ") mm")
        Debug.Print("  Max = (" & vBox(3) * 1000.0# & ", " & vBox(4) * 1000.0# & ", " & vBox(5) * 1000.0# & ") mm")
    End Sub

    Sub Main()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\key pad_1.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssy = swModel
        swModelDocExt = swModel.Extension

        ' Print the two diagonal corner points
        ' of the bounding box before modifying the
        ' assembly
        Debug.Print("Before:")
        ProcessAssyBox(swApp, swAssy)

        ' Change a dimension of one of the assembly components
        status = swModelDocExt.SelectByID2("Sketch1@Pad_1-1@key pad_1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("D1@Sketch1@Pad_1-1@key pad_1", "DIMENSION", 0.00306153201295202, 0.0373842545521677, -0.0323079625553351, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swDimension = swModel.Parameter("D1@Sketch1@pad_1.Part")
        errors = swDimension.SetSystemValue3(0.04, swSetValueInConfiguration_e.swSetValue_InThisConfiguration, Nothing)
        swModel.ClearSelection2(True)

        ' Update the bounding box
        swAssy.UpdateBox()

        ' Print the two diagonal corner points of the
        ' bounding box after modifying the assembly
        Debug.Print("After:")
        ProcessAssyBox(swApp, swAssy)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
