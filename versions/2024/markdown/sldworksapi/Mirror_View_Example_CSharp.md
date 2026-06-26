---
title: "Mirror View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_View_Example_CSharp.htm"
---

# Mirror View Example (C#)

This example shows how to mirror a view.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Verify that the drawing to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Mirrors the drawing view.
// 3. Examine the drawing and Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//-------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
```

```
namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            DrawingDoc swDrawing = default(DrawingDoc);
            View swView = default(View);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool mirrored = false;
            int orientation = 0;
```

```
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.slddrw";
            swDrawing = (DrawingDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swView = (View)swDrawing.GetFirstView(); //This is the drawing template
            swView = (View)swView.GetNextView(); //This is the first drawing view in the drawing
            swView.SetMirrorViewOrientation(true, (int)swMirrorViewPositions_e.swMirrorViewPosition_Horizontal);
            swView.GetMirrorViewOrientation(out mirrored, out orientation);
            Debug.Print("Mirrored? " + mirrored);
            Debug.Print("Orientation (0 = horizontal)? " + orientation);
```

```
        }
```

```
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
