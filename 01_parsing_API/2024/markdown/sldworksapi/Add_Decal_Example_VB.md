---
title: "Add Decal Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Decal_Example_VB.htm"
---

# Add Decal Example (VBA)

This example shows how to add a decal to a selected face on a part.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Verify that the specified decal files exist.
' 3. Verify that a ray-trace rendering engine is active.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects the face where to apply a decal.
' 3. Applies a decal to the selected face.
' 4. Gets the properties of the decal and prints them
'    to the Immediate window.
' 5. Examine the graphics area and the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

```
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFace As SldWorks.Face2
Dim swDecal As SldWorks.Decal
Dim swMaterial As SldWorks.RenderMaterial
Dim swFaceDecalPropertiesArray As Variant
Dim swFaceDecalProperties As SldWorks.FaceDecalProperties
Dim status As Boolean
Dim strname As String
Dim nDecalID As Long
Dim i As Long
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim nbrDecals As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks

    'Open part document and select face where to
    'apply a decal
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\minimum_clearance\top_plate.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -3.74778769440809E-03, 6.09129688728558E-02, 1.60000000000196E-02, False, 0, Nothing, 0)
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
```

```
    'Create the decal
    Set swDecal = swModelDocExt.CreateDecal
    Set swMaterial = swDecal
    status = swMaterial.AddEntity(swFace)
    strname = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\graphics\Decals\Logos\sw.p2d"
    swMaterial.fileName = strname
    strname = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\graphics\Decals\Logos\sw.bmp"
    swMaterial.TextureFilename = strname
    swMaterial.MappingType = 0
    swMaterial.FixedAspectRatio = False
    swMaterial.FitHeight = True
    swMaterial.FitWidth = True
    status = swModelDocExt.AddDecal(swDecal, nDecalID)
```

```
    'Rebuild the model
    Call swModelDocExt.Rebuild(swRebuildAll)
```

```
    'Get decal properties
    status = swModelDocExt.SelectByID2("", "FACE", -3.74778769440809E-03, 6.09129688728558E-02, 1.60000000000196E-02, False, 0, Nothing, 0)
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    nbrDecals = swFace.GetDecalsCount
    Debug.Print "Number of decals applied to this face: " & nbrDecals
    If nbrDecals > 0 Then
        swFaceDecalPropertiesArray = swFace.GetAllDecalProperties
        For i = 0 To UBound(swFaceDecalPropertiesArray)
            Set swFaceDecalProperties = swFaceDecalPropertiesArray(i)
            Debug.Print "Decal " & i + 1 & "'s texture:"
            Debug.Print "  Angle: " & swFaceDecalProperties.TextureAngle
            Debug.Print "  Angle UV: " & swFaceDecalProperties.TextureAngleUV
            Debug.Print "  File: "
            Debug.Print "     Name: " & swFaceDecalProperties.TextureFilename
            Debug.Print "     ID: " & swFaceDecalProperties.TextureFilenameID
            Debug.Print "  ID: " & swFaceDecalProperties.TextureID
            Debug.Print "  Map ID: " & swFaceDecalProperties.TextureMapID
            Debug.Print "  Mirrored? " & swFaceDecalProperties.TextureMirrored
            Debug.Print "  Render mode (0 = Image; 1 = Luminance):  " & swFaceDecalProperties.TextureRenderMode
            Debug.Print "  Translation: "
            Debug.Print "      U: " & swFaceDecalProperties.TextureTranslationU
            Debug.Print "      V: " & swFaceDecalProperties.TextureTranslationV
            Debug.Print "      X: " & swFaceDecalProperties.TextureTranslationX
            Debug.Print "      Y: " & swFaceDecalProperties.TextureTranslationY
            Debug.Print "  UV scale: "
            Debug.Print "      U: " & swFaceDecalProperties.TextureUScale
            Debug.Print "      V: " & swFaceDecalProperties.TextureVScale
        Next i
    End If
```

```
End Sub
```
