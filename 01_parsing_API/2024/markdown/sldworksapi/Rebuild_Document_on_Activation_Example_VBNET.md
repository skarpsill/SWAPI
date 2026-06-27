---
title: "Rebuild a Document on Activation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_Document_on_Activation_Example_VBNET.htm"
---

# Rebuild a Document on Activation Example (VB.NET)

This example shows how to activate and rebuild an assembly document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly.
 ' 2. Replace loaded_document with the assembly name.
 ' 3. Right-click a part in the FeatureManager design tree.
 ' 4. Select Open Part from the toolbar.
 ' 5. Edit a feature in the part.
 ' 6. Click OK in the PropertyManager to accept the changes.
 '
 ' Postconditions:
 ' 1. Displays a dialog.
 ' 2. Click Yes to rebuild the assembly.
 ' 3. Activates the assembly document.
 ' 4. Inspect the Immediate Window.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim Errors As Long

     Sub main()

         Dim bValue As Boolean
         Dim nValue As swRebuildOnActivation_e

         ' Set user preference to not rebuild on activation
         bValue = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swRebuildOnActivation, swRebuildOnActivation_e.swDontRebuildActiveDoc)
         Debug.Print("Rebuild user preference set to not rebuild on activation: " & bValue)

         nValue = swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swRebuildOnActivation)
         Debug.Print("swRebuildOnActivation_e user preference is: " & nValue)

         ' Ignore the user preference just set
         Debug.Print("Ignoring rebuild user preference.")

         ' Activate the loaded document and prompt for rebuild if the model is changed
         swModel = swApp.ActivateDoc3("loaded_document", False, swRebuildOnActivation_e.swUserDecision, Errors)
         Debug.Print("Error code after document activation: " + Errors.ToString)

     End Sub

     Public swApp As SldWorks

 End  Class
```
