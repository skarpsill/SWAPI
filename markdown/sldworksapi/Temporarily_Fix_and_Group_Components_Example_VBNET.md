---
title: "Temporarily Fix and Group Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Temporarily_Fix_and_Group_Components_Example_VBNET.htm"
---

# Temporarily Fix and Group Components Example (VB.NET)

This example shows how to temporarily fix and group components.

```
'-----------------------------------------------------------------------
' Preconditions: Verify that the specified assembly exists.
'
' Postconditions:
' 1. Opens the specified assembly, changes the view orientation to
'    dimetric, and zooms and fits the assembly in the graphics area.
' 2. Selects the rocker-1@valve_cam component.
'    a. Temporarily changes the rocker-1@valve_cam component from
'       floating to fixed, which is indicated by (f)* appearing before
'       rocker-1@value_cam in the FeatureManager design tree and
'       the pink component in the graphics area.
'    b. Press F5 after examining the FeatureManager design tree and
'       graphics area.
'    c. Changes the rocker-1@valve_cam component back to floating.
' 3. Selects the rocker-1@valve_cam and camshaft-1@valve_cam
'    components.
'    a. Temporarily groups the rocker-1@valve_cam and
'       camshaft-1@valve_cam components, which is indicated by
'       the pink components in the graphics area.
'    b. Press F5 after examining the graphics area.
'    c. Ungroups the rocker-1@valve_cam and camshaft-1@valve_cam
'       components.
' 4. Examine both the FeatureManager design tree and graphics area to
'    verify steps 2.c and 3.c.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssembly As AssemblyDoc
        Dim swModelDocExt As ModelDocExtension
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssembly = swModel
        swModelDocExt = swModel.Extension
        swModel.ShowNamedView2("*Dimetric", 9)
        swModel.ViewZoomtofit2()

        swModel.ClearSelection2(True)

        'Temporarily fix a component
        status = swModelDocExt.SelectByID2("rocker-1@valve_cam", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

        swAssembly.TemporaryFixGroup()

        Stop
        'Examine rocker-1@valve_cam in the FeatureManager design tree and graphics area
        '(f)* and the pink component indicate that the component is fixed
        'Press F5

        'Changes the component back to floating
        swAssembly.TemporaryFixGroupExit()

        swModel.ClearSelection2(True)

        'Temporarily group components
        status = swModelDocExt.SelectByID2("camshaft-1@valve_cam", "COMPONENT", 0, 0, 0, True, 2, Nothing, 0)
        status = swModelDocExt.SelectByID2("rocker-1@valve_cam", "COMPONENT", 0, 0, 0, True, 2, Nothing, 0)
        swAssembly.TemporaryFixGroup()

        Stop
        'Examine the graphics area
        'Pink components indicate that the components are grouped
        'Press F5

        'Ungroup components
        swAssembly.TemporaryFixGroupExit()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
