---
title: "Add Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Components_Example_VB.htm"
---

# Add Components Example (VBA)

This example shows how to add multiple components to an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a new part document.
 '    a. Extrude a rectangular block and cut-extrude a diagonal section
'      off one face of the block.
 '    b. Click Insert > Reference Geometry > Coordinate System.
 '    c. Select a corner of the block for the origin of the new coordinate system.
 '    d. Select an edge for the Z axis of the coordinate system.
 '    e. Click the green check mark to save the coordinate system.
 '       Coordinate System1 appears in the FeatureManager design tree.
 '    f. Save and minimize the part.
 ' 2. Replace <component_name> in the code with the full path name
'    of the new part.
 ' 3. Create a new assembly document.
 '    a. Create a line segment sketch originating at some distance
'       from the default origin of the assembly document.
 '    b. Click Insert > Reference Geometry > Coordinate System.
 '    c. Select one end point of the line segment for the origin
'       of the new coordinate system.
 '    d. Select the line segment for the X axis of the coordinate system.
 '    e. Click the green check mark to save the coordinate system.
 '       Coordinate System1 appears in the FeatureManager design tree.
 '    f. Right-click on Coordinate System1 in the FeatureManager design tree,
'       select Feature Properties, and rename the coordinate system
'       and its description to differ from Coordinate System1.
 '    g. Save the assembly and keep it open.
 '
 ' Postconditions:
 ' Component part is inserted into the assembly such that
 ' the part's Coordinate System1 is coincident (no translation or rotation)
 ' with the assembly's default (not user-defined) coordinate system.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim assemb As SldWorks.Assembly
 Dim compNames(0) As String
 Dim compXforms(15) As Double
 Dim compCoordSysNames(0) As String
 Dim vcompNames As Variant
 Dim vcompXforms As Variant
 Dim vcompCoordSysNames As Variant
 Dim vcomponents As Variant
Option Explicit
Sub main()
Set swApp = Application.SldWorks
 Set assemb = swApp.ActiveDoc

' For each component to be added, create a separate transform
If (Not assemb Is Nothing) Then
    compNames(0) = "<component_name>"
' Define the transformation matrix. See the IMathTransform API documentation.
' Add a rotational diagonal unit matrix (zero rotation) to the transformation matrix
     compXforms(0) = 1#
     compXforms(1) = 0#
     compXforms(2) = 0#
     compXforms(3) = 0#
     compXforms(4) = 1#
     compXforms(5) = 0#
     compXforms(6) = 0#
     compXforms(7) = 0#
     compXforms(8) = 1#
' Add a translation vector to the transformation matrix
     compXforms(9) = 0#
     compXforms(10) = 0#
     compXforms(11) = 0#
' Add a scaling factor to the transform
     compXforms(12) = 1#
' The last three elements of the transformation matrix are unused
' Register the component's coordinate system name
     compCoordSysNames(0) = "Coordinate System1"
  ' Add the component to the assembly.
   vcompNames = compNames
   vcompXforms = compXforms
   'vcompXforms = Nothing  ' also achieves zero rotation and translation of component
   vcompCoordSysNames = compCoordSysNames
   vcomponents = assemb.AddComponents3((vcompNames), (vcompXforms), (vcompCoordSysNames))
End If
End Sub
```
