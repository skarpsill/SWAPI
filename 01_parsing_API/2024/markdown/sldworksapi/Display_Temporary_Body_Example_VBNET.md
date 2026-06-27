---
title: "Display Temporary Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Temporary_Body_Example_VBNET.htm"
---

# Display Temporary Body Example (VB.NET)

This example shows how to display a temporary body.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to
'    open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects a component for the temporary body.
' 3. Displays the temporary body.
' 4. Examine the graphics area and the Immediate
'    window.
'
' NOTE: Because the assembly is used elsewhere, do
' not save changes.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim Part As ModelDoc2
        Dim Body As Body2
        Dim BodyCopy As Body2
        Dim status As Boolean
        Dim Component As Component2
        Dim MathUtility As MathUtility
        Dim MathXform As MathTransform
        Dim Xform(15) As Double
        Dim vXform As Object
        Dim retval As Integer
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        Xform(0) = 1.0#
        Xform(1) = 0.0#
        Xform(2) = 0.0#
        Xform(3) = 0.0#
        Xform(4) = 1.0#
        Xform(5) = 0.0#
        Xform(6) = 0.0#
        Xform(7) = 0.0#
        Xform(8) = 1.0#
        Xform(9) = 0.15
        Xform(10) = 0.0#
        Xform(11) = 0.0#
        Xform(12) = 1.0#
        Xform(13) = 0.0#
        Xform(14) = 0.0#
        Xform(15) = 0.0#
        vXform = Xform

        MathUtility = swApp.GetMathUtility
        MathXform = MathUtility.CreateTransform(vXform)

        'Open assembly
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem1.sldasm"
        Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select component and create temporary body
        status = Part.Extension.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        Component = Part.SelectionManager.GetSelectedObjectsComponent3(1, 0)
        Body = Component.GetBody
        BodyCopy = Body.Copy
        BodyCopy.ApplyTransform(MathXform)

        'Display temporary body
        retval = BodyCopy.Display3(Component, 255, swTempBodySelectOptions_e.swTempBodySelectable)
        Debug.Print("Temporary body displayed (0 = success)? " & retval)

        Part.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
