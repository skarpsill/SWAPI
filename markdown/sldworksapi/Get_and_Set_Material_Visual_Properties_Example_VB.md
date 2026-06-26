---
title: "Get and Set Material Visual Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Material_Visual_Properties_Example_VB.htm"
---

# Get and Set Material Visual Properties Example (VBA)

This method shows how to get and set the material properties of a part.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets the part's material visual properties.
' 2. Inspect the Immediate window and graphics area.
'------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim myModel As SldWorks.ModelDoc2
     Dim myPart As SldWorks.PartDoc
     Dim myMatVisProps As SldWorks.MaterialVisualPropertiesData
     Dim configName As String, databaseName As String
     Dim newPropName As String
     Dim orgBlend As Boolean, orgApply As Boolean
     Dim orgAngle As Double
     Dim orgScale As Double
     Dim longstatus As Long
    Set swApp = Application.SldWorks
     Set myModel = swApp.ActiveDoc
     Set myPart = myModel
     Set myMatVisProps = myPart.GetMaterialVisualProperties()
    Debug.Print "===== Material Visual Properties Example ====="
    If Not myMatVisProps Is Nothing Then
         Call dump_material_visual_properties(myMatVisProps, myPart)
        ' Set the material to something else, so that the display changes
        configName = "default"
         databaseName = "SOLIDWORKS Materials"
         newPropName = "Beech"
         myPart.SetMaterialPropertyName2 configName, databaseName, newPropName
         Call dump_material_visual_properties(myMatVisProps, myPart)
     End If
    ' Set the material visual properties to be just color, no advanced graphics
    Set myMatVisProps = myPart.GetMaterialVisualProperties()
    If Not myMatVisProps Is Nothing Then
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)

        ' Set the material visual properties to be RealView
         myMatVisProps.RealView = True
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
```

```vb
   ' Set the material visual properties to be SOLIDWORKS standard textures
```

```vb
        myMatVisProps.RealView = False
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
     End If
    Set myMatVisProps = myPart.GetMaterialVisualProperties()
    If Not myMatVisProps Is Nothing Then
         orgAngle = myMatVisProps.Angle
         myMatVisProps.Angle = orgAngle + 1#
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
         orgScale = myMatVisProps.Scale2
         myMatVisProps.Scale2 = orgScale * 1.25
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
        ' Toggle the standard texture to blend with the part color
        If myMatVisProps.BlendColor = 0 Then
             orgBlend = False
         Else
             orgBlend = True
         End If
        myMatVisProps.BlendColor = Not orgBlend
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
         myMatVisProps.BlendColor = orgBlend
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
        ' Toggle the apply material color to part flag
        If myMatVisProps.ApplyMaterialColorToPart = 0 Then
             orgApply = False
         Else
             orgApply = True
         End If
        myMatVisProps.ApplyMaterialColorToPart = Not orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
         myMatVisProps.ApplyMaterialColorToPart = orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
        ' Toggle the apply material hatch to drawing section view flag
        If myMatVisProps.ApplyMaterialHatchToSection = 0 Then
             orgApply = False
         Else
             orgApply = True
         End If
        myMatVisProps.ApplyMaterialHatchToSection = Not orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
         myMatVisProps.ApplyMaterialHatchToSection = orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)

        ' Toggle the apply appearance flag
         If myMatVisProps.ApplyAppearance = 0 Then
             orgApply = False
         Else
             orgApply = True
         End If
        myMatVisProps.ApplyAppearance = Not orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
         myMatVisProps.ApplyAppearance = orgApply
         longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, swThisConfiguration, Nothing)
         Call dump_material_visual_properties(myMatVisProps, myPart)
     End If
End Sub
Private Sub dump_material_visual_properties(myMatVisProps As SldWorks.MaterialVisualPropertiesData, myPart As SldWorks.PartDoc)
     Dim configName As String, databaseName As String
     Dim propName As String
     Dim bRealView As Boolean
     Dim dScale As Double, dAngle As Double
     Dim bBlendColor As Boolean, bApplyColor As Boolean, bApplyHatch As Boolean, bApplyAppearance As Boolean
     configName = "default"
     propName = myPart.GetMaterialPropertyName2(configName, databaseName)
     Debug.Print ""
     Debug.Print "Config: """ & configName & """, Database: """ & databaseName & """, Material: """ & propName & """"
    If Not myMatVisProps Is Nothing Then
         bRealView = myMatVisProps.RealView
         dScale = myMatVisProps.Scale2
         dAngle = myMatVisProps.Angle
         bBlendColor = myMatVisProps.BlendColor
         bApplyColor = myMatVisProps.ApplyMaterialColorToPart
         bApplyHatch = myMatVisProps.ApplyMaterialHatchToSection
         bApplyAppearance = myMatVisProps.ApplyAppearance

         If bRealView = 0 Then
             Debug.Print "Advanced graphics - SOLIDWORKS standard textures."
         Else
             Debug.Print "Advanced graphics - RealView textures."
         End If
         Debug.Print "   SOLIDWORKS standard texture scale = " & dScale & ", Angle = " & dAngle
         If bBlendColor = 0 Then
             Debug.Print "   Do not blend part color with SOLIDWORKS standard texture."
         Else
              Debug.Print "   Blend part color with SOLIDWORKS standard texture."
         End If

        If bApplyColor = 0 Then
             Debug.Print "Do not apply material color to part."
         Else
             Debug.Print "Apply material color to part."
         End If
        If bApplyHatch = 0 Then
             Debug.Print "Do not apply material hatch to drawing section."
         Else
             Debug.Print "Apply material hatch to drawing section."
        End If
         If bApplyAppearance = 0 Then
             Debug.Print "Do not apply appearance."
         Else
             Debug.Print "Apply appearance."
         End If
    End If
End Sub
```
