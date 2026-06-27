---
title: "Insert MidSurface in Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_MidSurface_in_Component_Example_VBNET.htm"
---

# Insert MidSurface in Component Example (VB.NET)

This example shows how to insert a midsurface feature in a component.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly that contains at least one component
'    that contains a solid body.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a midsurface feature in the component.
' 2. Gets the number of faces in the midsurface feature.
' 3. Examine the Immediate window.
' 4. Expand the component in the FeatureManager design tree
'    in which the midsurface feature was inserted to
'    verify step 1.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swExt As ModelDocExtension
    Dim swSelMgr As SelectionMgr
    Dim swComp As Component2
    Dim swAssem As AssemblyDoc
    Dim featMgr As FeatureManager

    Public Sub main()

        swModel = swApp.ActiveDoc
        swExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        featMgr = swModel.FeatureManager
        swAssem = swModel
        Dim vComponents As Object
        vComponents = swAssem.GetComponents(True)
        swComp = vComponents(0)
        Dim vBodies As Object
        vBodies = swComp.GetBodies2(swBodyType_e.swSolidBody)
        If Not IsNothing(vBodies) Then
            Dim pBody As Body2
            pBody = vBodies(0)
            Dim midSurf As MidSurface3
            swModel = swComp.GetModelDoc2
            Debug.Print("Component in which to insert midsurface feature: " & swModel.GetPathName)
            midSurf = featMgr.InsertMidSurface(pBody, swModel, 0.5, True)
            Debug.Print("Face count: " & midSurf.GetFaceCount)
        Else
            Debug.Print("Open a different assembly in which the specified body is a solid body.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
