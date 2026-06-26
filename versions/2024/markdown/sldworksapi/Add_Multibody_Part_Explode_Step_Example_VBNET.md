---
title: "Add Multibody Part Explode Step Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Multibody_Part_Explode_Step_Example_VBNET.htm"
---

# Add Multibody Part Explode Step Example (VB.NET)

This example shows how to create an explode view of a multibody part.

```vb
  '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\multibody\multi_Inter.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Exploded View1 in ConfigurationManager.
 ' 2. Adds Chain1 to Exploded View1.
 ' 3. Displays the Exploded View1 in its exploded state.
 ' 4. Inspect the Immediate window, the ConfigurationManager,
 '      and the graphics area.
 '
 ' Note: Because the model is used elsewhere, do not save any changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
```

```vb
 Partial  Class  SolidWorksMacro
```

```vb
       Sub main()
```

```vb
            Dim swModel  As  PartDoc
```

```vb
            Dim config  As  Configuration
```

```vb
            Dim configName  As  String
```

```vb
            Dim swMdl  As  ModelDoc2
```

```vb
            Dim explStep  As  PartExplodeStep
```

```vb
            Dim comp  As  Body2
```

```vb
            Dim var  As  Object
```

```vb
            Dim varViews  As  Object
```

```vb
            Dim configVar  As  Object
```

```vb
            Dim boolstatus  As  Boolean
```

```vb
            Dim i  As  Long
```

```vb
            Dim errCode  As  Long
```

```vb
             swModel = swApp.ActiveDoc
```

```vb
             swMdl = swModel
```

```vb
             configVar = swMdl.GetConfigurationNames
```

```vb
            Call swModel.CreateExplodedView
```

```vb
             varViews = swModel.GetExplodedViewNames(configVar(0))
```

```vb
             configName = swModel.GetExplodedViewConfigurationName(varViews(0))
```

```vb
             config = swMdl.GetConfigurationByName(configName)
```

```vb
             swModel.ShowExploded(True, varViews(0))
```

```vb
          'Select the bodies to move
```

```vb
             boolstatus = swMdl.Extension.SelectByID2("Extrude-Thin1",  "SOLIDBODY", 0, 0, 0,  True, 1,  Nothing, 0)
```

```vb
            'Add an explode step without selecting an explode direction entity
```

```vb
            'Defaults to the Z-direction manipulator index
```

```vb
             explStep = config.AddPartExplodeStep("Exploded View1", 0.07, -1,  False,  True, errCode)
```

```vb
            Call swMdl.EditRebuild3
```

```vb
            'Get bodies moved in the explode step
```

```vb
             var = explStep.GetBodies()
```

```vb
            Debug.Print("Explode view: " & varViews(0))
```

```vb
            Debug.Print("Explode step: " & explStep.Name)
```

```vb
            Debug.Print("Explode distance (m): " & explStep.ExplodeDistance)
```

```vb
            Debug.Print("Reverse translation direction? " & explStep.ReverseTranslationDirection)
```

```vb
            Debug.Print("Automatically space components on drag? " & explStep.AutoSpaceBodiesOnDrag)
```

```vb
            Debug.Print("Bodies moved in the explode step:")
```

```vb
            For i = 0  To UBound(var)
```

```vb
                comp = var(i)
```

```vb
               Debug.Print("    " & comp.Name)
```

```vb
            Next
```

```vb
       End  Sub
```

```vb
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
