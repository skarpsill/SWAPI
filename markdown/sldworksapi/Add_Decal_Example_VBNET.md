---
title: "Add Decal Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Decal_Example_VBNET.htm"
---

# Add Decal Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swModelDocExt As ModelDocExtension
        Dim swFace As Face2
        Dim swDecal As Decal
        Dim swMaterial As RenderMaterial
        Dim swFaceDecalPropertiesArray() As Object
        Dim swFaceDecalProperties As FaceDecalProperties
        Dim status As Boolean
        Dim strname As String
        Dim nDecalID As Integer
        Dim i As Integer
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim nbrDecals As Integer

        'Open part document and select face where to
        'apply a decal
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\minimum_clearance\top_plate.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swSelMgr = swModel.SelectionManager
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.00374778769440809, 0.0609129688728558, 0.0160000000000196, False, 0, Nothing, 0)
        swFace = swSelMgr.GetSelectedObject6(1, -1)
        swModel.ClearSelection2(True)

        'Create the decal
        swDecal = swModelDocExt.CreateDecal
        swMaterial = swDecal
        status = swMaterial.AddEntity(swFace)
        strname = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\graphics\Decals\Logos\sw.p2d"
        swMaterial.FileName = strname
        strname = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\graphics\Decals\Logos\sw.bmp"
        swMaterial.TextureFilename = strname
        swMaterial.MappingType = 0
        swMaterial.FixedAspectRatio = False
        swMaterial.FitHeight = True
        swMaterial.FitWidth = True
        status = swModelDocExt.AddDecal(swDecal, nDecalID)

        'Rebuild the model
        Call swModelDocExt.Rebuild(swRebuildOptions_e.swRebuildAll)

        'Get decal properties
        status = swModelDocExt.SelectByID2("", "FACE", -0.00374778769440809, 0.0609129688728558, 0.0160000000000196, False, 0, Nothing, 0)
        swFace = swSelMgr.GetSelectedObject6(1, -1)
        nbrDecals = swFace.GetDecalsCount
        Debug.Print("Number of decals applied to this face: " & nbrDecals)
        If nbrDecals > 0 Then
            swFaceDecalPropertiesArray = swFace.GetAllDecalProperties
            For i = 0 To UBound(swFaceDecalPropertiesArray)
                swFaceDecalProperties = swFaceDecalPropertiesArray(i)
                Debug.Print("Decal " & i + 1 & "'s texture:")
                Debug.Print("  Angle: " & swFaceDecalProperties.TextureAngle)
                Debug.Print("  Angle UV: " & swFaceDecalProperties.TextureAngleUV)
                Debug.Print("  File: ")
                Debug.Print("     Name: " & swFaceDecalProperties.TextureFilename)
                Debug.Print("     ID: " & swFaceDecalProperties.TextureFilenameID)
                Debug.Print("  ID: " & swFaceDecalProperties.TextureID)
                Debug.Print("  Map ID: " & swFaceDecalProperties.TextureMapID)
                Debug.Print("  Mirrored? " & swFaceDecalProperties.TextureMirrored)
                Debug.Print("  Render mode (0 = Image; 1 = Luminance):  " & swFaceDecalProperties.TextureRenderMode)
                Debug.Print("  Translation: ")
                Debug.Print("      U: " & swFaceDecalProperties.TextureTranslationU)
                Debug.Print("      V: " & swFaceDecalProperties.TextureTranslationV)
                Debug.Print("      X: " & swFaceDecalProperties.TextureTranslationX)
                Debug.Print("      Y: " & swFaceDecalProperties.TextureTranslationY)
                Debug.Print("  UV scale: ")
                Debug.Print("      U: " & swFaceDecalProperties.TextureUScale)
                Debug.Print("      V: " & swFaceDecalProperties.TextureVScale)
            Next i
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
