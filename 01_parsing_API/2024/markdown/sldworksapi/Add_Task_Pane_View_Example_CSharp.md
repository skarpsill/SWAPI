---
title: "Add Task Pane View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Task_Pane_View_Example_CSharp.htm"
---

# Add Task Pane View Example (C#)

This example shows how to add a tab to the Task Pane.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
// 1. Create bitmaps in 6 pixel sizes:
//    20 X 20
//    32 X 32
//    40 X 40
//    64 X 64
//    96 X 96
//    128 X 128
// 2. Replace the bitmap array elements in the macro to full pathnames of
//    these bitmap files.
 //
 // Postconditions:
 // 1. Examine the Task Pane.
// 2. Displays a tab on the Task Pane with an image that is appropriate for
//    the current screen resolution or operating system scale.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace AddTaskPaneView_CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            TaskpaneView ctrl;
            string[] bitmap = new string[6];
            string toolTip;

            bitmap[0] = "20x20_bitmap_pathname";
            bitmap[1] = "32x32_bitmap_pathname";
            bitmap[2] = "40x40_bitmap_pathname";
            bitmap[3] = "64x64_bitmap_pathname";
            bitmap[4] = "96x96_bitmap_pathname";
            bitmap[5] = "128x128_bitmap_pathname";
            toolTip = "";
            ctrl = swApp.CreateTaskpaneView3(bitmap, toolTip);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
