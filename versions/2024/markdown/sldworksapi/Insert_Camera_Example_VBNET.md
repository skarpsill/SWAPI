---
title: "Insert Camera Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Camera_Example_VBNET.htm"
---

# Insert Camera Example (VB.NET)

This example shows how to insert a camera and print out its settings.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a model document that does not have any cameras inserted.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a camera in the model document.
' 2. Click View > Lights and Cameras > Properties > Camera1.
' 3. Click Zoom to Fit.
' 4. Examine the Immediate window, the graphics area, and the
'    Camera1 PropertyManager page.
'-------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swCamera As Camera

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        ' Insert a camera
        swCamera = swModelDocExt.InsertCamera

        ' Print out camera settings
        Debug.Print("ID                                               = " & swCamera.ID)
        Debug.Print("Focal distance                                   = " & swCamera.GetFocalDistance * 1000.0# & " mm")
        Debug.Print("Perspective mode                                 = " & swCamera.Perspective)
        Debug.Print("Depth of field effects enabled                   = " & swCamera.DepthOfFieldEnabled)
        Debug.Print("Distance from focal plane to where focus is lost = " & swCamera.DepthOfFieldOffset * 1000.0# & " mm")
        Debug.Print("Horizontal angle of the field of view            = " & swCamera.FieldOfViewAngle * 1000.0# & " mm")
        Debug.Print("Depth of the field of view                       = " & swCamera.FieldOfViewDepth * 1000.0# & " mm")
        Debug.Print("Height of the field of view                      = " & swCamera.FieldOfViewHeight * 1000.0# & " mm")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
