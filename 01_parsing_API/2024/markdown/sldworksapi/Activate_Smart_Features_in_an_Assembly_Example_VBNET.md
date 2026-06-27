---
title: "Activate Smart Feature in an Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Smart_Features_in_an_Assembly_Example_VBNET.htm"
---

# Activate Smart Feature in an Assembly Example (VB.NET)

This example shows how to activate a Smart Feature in an assembly.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\testSmartAssembly.sldasm.
 '
 ' Postconditions:
 ' 1. Activates Smart Feature holecube-1 and creates two extruded cuts
 '    for the selected reference entity.
 ' 2. Displays Smart Feature holecube-1 in the FeatureManager design tree.
 ' 3. Creates Smart-Feature1 in component testpart100.
 ' 4. Expand and examine testpart100 and holecube-1 in the FeatureManager
 '    design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim feat As Feature
     Dim comp As Component2
     Dim comps As Object
     Dim selMgr As SelectionMgr
     Dim features As Object
     Dim config As Configuration
     Dim featuresSelected As Object
     Dim components As Object
     Dim componentsSelected As Object
     Dim references As Object
     Dim face As Face2
     Dim swAss As AssemblyDoc
     Dim doc As ModelDoc2
     Dim boolstatus As Boolean
     Dim i As  Long
     Dim j As  Long

     Sub main()

         swAss = swApp.ActiveDoc

         comps = swAss.GetComponents(True)

         doc = swAss
         selMgr = doc.SelectionManager

         For i = 0 To UBound(comps)

             comp = comps(i)
             If comp.IsSmartComponent Then

                 If comp.GetSmartComponentData(features, featuresSelected, components, componentsSelected, references) Then

                     If IsNothing(featuresSelected) = False Then
                         For j = 0 To UBound(featuresSelected)
                             If featuresSelected(j) = False Then
                                 featuresSelected(j) = True
                             End If
                         Next

                     End If

                     If IsNothing(componentsSelected) = False Then
                         For j = 0 To UBound(componentsSelected)
                             If featuresSelected(j) = False Then
                                 componentsSelected(j - 1) = True
                             End If
                         Next

                     End If

                     boolstatus = doc.Extension.SelectByID2("", "FACE", -0.1054255613309, -0.008376708432593, 0.03086069829328,  False, 0,  Nothing, 0)
                     face = selMgr.GetSelectedObject6(1, -1)
                     references(0) = face

                     Dim arrRefsIn(0) As DispatchWrapper
                     arrRefsIn(0) = New DispatchWrapper(references(0))
                     boolstatus = comp.SetSmartComponentData(featuresSelected, componentsSelected, (arrRefsIn))

                 End If

                 Debug.Print(comp.Name)

             End If

         Next

     End Sub

     Public swApp As SldWorks

 End  Class
```
