---
title: "Activate Smart Feature in an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Smart_Features_in_an_Assembly_Example_VB.htm"
---

# Activate Smart Feature in an Assembly Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim feat As SldWorks.Feature
 Dim comp As SldWorks.Component2
 Dim comps As Variant
 Dim selMgr As SelectionMgr
 Dim features As Variant
 Dim config As SldWorks.Configuration
 Dim featuresSelected As Variant
 Dim components As Variant
 Dim componentsSelected As Variant
 Dim references As Variant
 Dim face As SldWorks.Face2
 Dim swAss As SldWorks.AssemblyDoc
 Dim doc As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
 Dim i As Long
 Dim j As Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set swAss = swApp.ActiveDoc

    comps = swAss.GetComponents(True)

    Set doc = swAss
     Set selMgr = doc.SelectionManager

    For i = 0 To UBound(comps)

        Set comp = comps(i)
         If comp.IsSmartComponent Then

            If comp.GetSmartComponentData(features, featuresSelected, components, componentsSelected, references) Then

                If IsEmpty(featuresSelected) = False Then
                     For j = 0 To UBound(featuresSelected)
                         If featuresSelected(j) = False Then
                              featuresSelected(j) = True
                         End If
                      Next

                End If

                 If IsEmpty(componentsSelected) = False Then
                    For j = 0 To UBound(componentsSelected)
                         If featuresSelected(j) = False Then
                             componentsSelected(j - 1) = True
                         End If
                      Next

                End If

               boolstatus = swAss.Extension.SelectByID2("", "FACE", -0.1054255613309, -0.008376708432593, 0.03086069829328, False, 0, Nothing, 0)
                Set face = selMgr.GetSelectedObject(1)
                Set references(0) = face

               boolstatus = comp.SetSmartComponentData(featuresSelected, componentsSelected, references)

             End If

            Debug.Print comp.Name

        End If

    Next
End Sub
```
