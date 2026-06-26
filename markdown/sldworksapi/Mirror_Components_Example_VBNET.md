---
title: "Mirror Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Components_Example_VBNET.htm"
---

# Mirror Components Example (VB.NET)

This example shows how to mirror components in an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\advdrawings\98food processor.sldasm.
 '
 ' Postconditions:
 ' 1. Inserts reference plane PLANE4.
 ' 2. Creates feature MirrorComponent1 that mirrors six assembly
 '    components.
 ' 3. Saves the mirror components to files with file name suffix _TestMirror to
 '    public_documents\samples\tutorial\advdrawings.
 ' 4. Examine public_documents\samples\tutorial\advdrawings, the FeatureManager design
 '    tree, and the graphics area.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         swModel = swApp.ActiveDoc

         Dim boolstatus As Boolean
         boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.104250921669188, -0.000236987012272039, -0.0597199999999418,  True, 0,  Nothing, 0)
         Dim myRefPlane As RefPlane
         myRefPlane = swModel.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0)

         Dim swAssem As AssemblyDoc
         swAssem = swModel

         Dim compsToInstance As Object
         compsToInstance =  Nothing

         Dim filenames As Object
         filenames =  Nothing

         Dim location As String
         location =  ""

         Dim nameModifierType As swMirrorComponentNameModifier_e
         nameModifierType = swMirrorComponentNameModifier_e.swMirrorComponentName_Suffix
         Dim nameModifier As String
         nameModifier =  "_TestMirror"

         Dim mirrorPlane As Feature
         mirrorPlane = swAssem.FeatureByName("PLANE4")

         Dim compsToMirror(0 To 5) As Component2
         compsToMirror(0) = swAssem.GetComponentByName("gear- caddy-1")
         compsToMirror(1) = swAssem.GetComponentByName("middle-gear-1")
         compsToMirror(2) = swAssem.GetComponentByName("shaft gear-1")
         compsToMirror(3) = swAssem.GetComponentByName("middle-gear plate-1")
         compsToMirror(4) = swAssem.GetComponentByName("base plate-1")
         compsToMirror(5) = swAssem.GetComponentByName("shaft gear insert-1")

         Dim orientations As Object
         orientations =  Nothing

         Dim orientAboutCoM As Boolean
         orientAboutCoM =  True

         Dim createDerivedConfigs As Boolean
         createDerivedConfigs =  False

         Dim importOptions As Integer
         importOptions = swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids

         Dim breakLinks As Boolean
         breakLinks =  False
         Dim preserveZAxis As Boolean
         preserveZAxis =  True

         Dim vResult As Object
         vResult = swAssem.MirrorComponents3(mirrorPlane, compsToInstance, orientations, orientAboutCoM,(compsToMirror), createDerivedConfigs, filenames, nameModifierType, nameModifier, location, importOptions, breakLinks, preserveZAxis,  True)

     End Sub

     Public swApp As SldWorks

 End  Class
```
