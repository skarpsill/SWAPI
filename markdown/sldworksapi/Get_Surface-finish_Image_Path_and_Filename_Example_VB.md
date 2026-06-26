---
title: "Get Surface-finish Image Path and File Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm"
---

# Get Surface-finish Image Path and File Name Example (VBA)

This example shows how to set and get the path and file name of the image used for an appearance's surface finish.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified model document exists.
'    * specified materials and surface-finish image exist.
'    * a ray-trace rendering engine is loaded.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified model document.
' 2. Applies the specified appearance and surface finish to the model.
' 3. Gets the file names of the first appearance and surface finish
'    applied to the model.
' 4. If prompted to use perspective views in rendering, click
'    Continue without Camera or Perspective.
' 5. Renders the model.
' 6. Examine the Final Render and Immediate windows.
'
' NOTES:
' * Rendering can take several minutes to complete.
' * Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swComponent As SldWorks.Component2
Dim swConfiguration As SldWorks.Configuration
Dim swRenderMaterial As SldWorks.RenderMaterial
Dim swRayTraceRenderer As SldWorks.RayTraceRenderer
Dim nbrRenderMaterials As Long
Dim fileName As String
Dim warnings As Long
Dim errors As Long
Dim status As Boolean
Dim materialName As String
Dim displayStateNames() As String
Dim materialID1 As Long
Dim materialID2 As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    'Open model document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\offset\bushing.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Access the ray-trace rendering engine
    'Set swRayTraceRenderer = swApp.GetRayTraceRenderer()
```

```
    'Create material for the appearance
    materialName = "C:\Program Files\SolidWorks Corp\SolidWorks\data\graphics\Materials\metal\bronze\cast bronze.p2m"
    Set swModelDocExt = swModel.Extension
    Set swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName)
```

```
    'Verify that RealView Graphics is set
    Debug.Print "RealView Graphics set? " & swModelDocExt.ViewDisplayRealView
```

```
    'Add an appearance
    status = swModelDocExt.SelectByID2("bushing.SLDPRT", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swComponent = swSelectionMgr.GetSelectedObject6(1, -1)
    status = swRenderMaterial.AddEntity(swComponent)
    Debug.Print "Appearance added to model? " & status
```

```
    'Add surface finish
    fileName = "C:\Program Files\SolidWorks Corp\SolidWorks\data\Images\textures\metal\cast\cast_bump.jpg"
    swRenderMaterial.BumpTextureFilename = fileName
```

```
    swModel.ClearSelection2 True
```

```
    'Get the names of display states
    'Add the appearance to all of the display states
    Set swConfiguration = swModel.GetActiveConfiguration
    displayStateNames = swConfiguration.GetDisplayStates
    status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, swDisplayStateOpts_e.swAllDisplayState, displayStateNames, materialID1, materialID2)
```

```
    'Get the number of appearances
    nbrRenderMaterials = swModelDocExt.GetRenderMaterialsCount2(swDisplayStateOpts_e.swAllDisplayState, displayStateNames)
```

```
    'If one or more appearances are applied to the model,
    'then get the file names of the first appearance and surface finish applied
    If nbrRenderMaterials > 0 Then
        Debug.Print "First appearance's file name: " & swRenderMaterial.fileName
        Debug.Print "  Surface finish's file name: " & swRenderMaterial.BumpTextureFilename
        Debug.Print "Fixed aspect ratio? " & swRenderMaterial.FixedAspectRatio
        Debug.Print "  Width: " & swRenderMaterial.Width * 1000# & "mm"
        Debug.Print "  Height: " & swRenderMaterial.Height * 1000# & "mm"
        If Not swRenderMaterial.DoubleSided Then
            swRenderMaterial.DoubleSided = True
        End If
        Debug.Print "Double-sided? " & swRenderMaterial.DoubleSided
        swRenderMaterial.RoundSharpEdges = 0.005
        Debug.Print "Round sharp edges value: " & swRenderMaterial.RoundSharpEdges * 1000# & "mm"
```

```
        'Display final render window
        status = swRayTraceRenderer.InvokeFinalRender
    Else
        Debug.Print "No appearances applied to this model."
    End If

End Sub
```
