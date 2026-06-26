---
title: "Create Solid Body Surface Trim Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm"
---

# Create Solid Body Surface Trim Feature Example (VB.NET)

This example shows how to create a solid body surface trim feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Creates Surface-Trim1.
' 3. Expand and examine Solid Bodies(1) in the FeatureManager
'    design tree and examine the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim status As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SurfaceTrimFeature.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager

        ' Select surface features
        status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.0446486526100784, 0.0218350174377093, 0.0123754341749418, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.00815686270678384, 0.0415839719953865, 0.0242402652081068, True, 0, Nothing, 0)

        ' Select trimming surfaces to create solid body surface trim feature
        status = swFeatureManager.PreTrimSurface(True, True, False, True)
        status = swModelDocExt.SelectByID2("", "SURFACEBODY", 0.0059504253577245, 0.0413800871671199, 0.0248740287174201, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.037205042299604, 0.0343527327176432, 0.0123446167727934, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.0104497983190015, -0.047217217677548703, 0.0233436625590571, True, 0, Nothing, 0)
        Debug.Print("Solid body surface trim feature? " & swFeatureManager.SolidForTrim)
        swFeatureManager.SolidForTrim = True
        Debug.Print("Solid body surface trim feature? " & swFeatureManager.SolidForTrim)
        swFeature = swFeatureManager.PostTrimSurface(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
