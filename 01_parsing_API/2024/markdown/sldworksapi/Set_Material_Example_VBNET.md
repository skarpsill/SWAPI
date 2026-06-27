---
title: "Set Material Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Material_Example_VBNET.htm"
---

# Set Material Example (VB.NET)

This example shows how to get the names of the material schema, material
databases, and bodies in a part document. This example also shows how
to apply a SOLIDWORKS Material to all of the bodies in akadov_tag{{<spaces>}}kadov_tag{{</spaces>}}part
document.

```vb
'----------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part document.
 ' 2. Applies the material ABS PC (polycarbonate plastic)
 '    from the SOLIDWORKS Material database to all
 '    bodies in the part.
 ' 3. To verify, examine:
 '    * DisplayManager tab
 '    * graphics area
 '    * Immediate window
 '
 ' NOTE: Because the part document is used elsewhere,
 ' do not save changes.
 '----------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swPart As PartDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swBody As Body2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errors As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim warnings As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vMatDBarr As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vMatDB As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Bodies As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BodyMaterialError As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sMatName As String = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sMatDB As String = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim itr As Integer
         Dim boolstat as Boolean

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open the document
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swDocumentTypes_e.swDocPART,
 swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the material schema and names
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' of available materials databases
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vMatDBarr = swApp.GetMaterialDatabases
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Material schema pathname = " & swApp.GetMaterialSchemaPathName)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For Each vMatDB In vMatDBarr
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Material database: " & vMatDB)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Bodies = swPart.GetBodies2(swBodyType_e.swAllBodies, False)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For itr = 0 To UBound(Bodies)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swBody = Bodies(itr)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get the name of the body
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(swBody.Name)

             boolstat = swBody.Select2(False, Nothing)

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Set the SOLIDWORKS material for that body
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BodyMaterialError = swBody.SetMaterialProperty("Default", "solidworks materials.sldmat",
 "ABS PC")
             ' Comment out previous statement and uncomment following statement to use custom material
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'BodyMaterialError = swBody.SetMaterialProperty("Default", "custom materials.sldmat",
 "Custom Plastic")

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get the names of the body's material and the
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' database to which it belongs
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sMatName = swBody.GetMaterialPropertyName("", sMatDB)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If sMatName = "" Then
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Body " & itr & "'s material name: No material applied")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Body " & itr & "'s material name: " & sMatName)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Body " & itr & "'s material database: " & sMatDB)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" ")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next itr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
