---
title: "Get Annotations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotations_Example_CSharp.htm"
---

# Get Annotations Example (C#)

This example shows how to get the annotations of a model.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model with one or more annotations.
 // 2. Open an Immediate window.
 //
 // Postconditions: All the annotations are printed in the Immediate window.
 //----------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetAnnotations_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel;
             ModelDocExtension swModelDocExt;
             Annotation swAnnotation;
             int iAnnoCnt;
             Object[] arrAnnotation;
             int IAnnoType;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             iAnnoCnt = swModelDocExt.GetAnnotationCount();

             if (iAnnoCnt > 0)
             {
                 arrAnnotation = (Object[])swModelDocExt.GetAnnotations();

                 for (int i = 0; i <= arrAnnotation.Length - 1; i++)
                 {
                     swAnnotation = (Annotation)arrAnnotation[i];

                     IAnnoType = swAnnotation.GetType();

                     switch (IAnnoType)
                     {
                         case 1:
                             Debug.Print("Annotation: Thread");
                             break;
                         case 2:
                             Debug.Print("Annotation: Datum Tag");
                             break;
                         case 3:
                             Debug.Print("Annotation: Datum Target Symbol");
                             break;
                         case 4:
                             Debug.Print("Annotation: Display Diamension");
                             break;
                         case 5:
                             Debug.Print("Annotation: Gtol");
                             break;
                         case 6:
                             Debug.Print("Annotation: Note");
                             break;
                         case 7:
                             Debug.Print("Annotation: SFS Symbol");
                             break;
                         case 8:
                             Debug.Print("Annotation: Weld Symbol");
                             break;
                         case 9:
                             Debug.Print("Annotation: Custom Symbol");
                             break;
                         case 10:
                             Debug.Print("Annotation: Dowel Symbol");
                             break;
                         case 11:
                             Debug.Print("Annotation: Leader");
                             break;
                         case 12:
                             Debug.Print("Annotation: Block");
                             break;
                         case 13:
                             Debug.Print("Annotation: Center Mark symbol");
                             break;
                         case 14:
                             Debug.Print("Annotation: Table Annotation");
                             break;
                         case 15:
                             Debug.Print("Annotation: Center Line ");
                             break;
                         case 16:
                             Debug.Print("Annotation: Datum Origin");
                             break;
                     }
                 }
             }
         }

         public SldWorks swApp;
     }
 }
```
