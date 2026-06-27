---
title: "Record SOLIDWORKS Macro"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Record_Solidworks_Macro.htm"
---

# Record SOLIDWORKS Macro

#### To record a SOLIDWORKS macro:

1. ClickRecord\Pause
  Macroon the Macro toolbar, or clickTools,Macro,Record.
2. Perform the actions that you want to record.
3. When you are done recording, clickStop
  Macroon the Macro toolbar or clickTools,Macro,Stop.
4. In the dialog, type a name for the macro inFile name, select the type of macro
  inSave as type, and clickSave.

NOTES:

- [SOLIDWORKS 2018 offers Visual Studio Tools for
  Applications (VSTA)](VSTA_2015.htm).
- If you selectedSW VBA Macros (*.swp), then the.swpextension is automatically added
  to the filename.
- If you selectedSW VSTA VB Macro (*.vbproj), then a
  Visual Basic .NET project is created. Building or debugging the project
  creates an executable file with an filename extension of.dll.
- If you selectedSW VSTA C# Macro (*.csproj), then a
  C# project is created. Building or debugging the project creates an executable
  file with an filename extension of.dll.
- If you selectedSW All Macros Types(*.swp,
  *.csproj, *.vbproj),
  then a VBA macro file is created and VB.NET, and C# projects are created.
  A .swpextension is automatically
  added to the VBA macro's filename. Two folders are created for the VB.NET
  and C# projects.
- The VB.NET project
  folder's name is the name of the macro plus-vbnet.
- The C# project folder
  name is the name of the project plus-csharp.

  For example, if you saved the just recorded macro asMacro1and selectedSW All Macros Types (*.swp,
  *.csproj, *.vbproj)inSave as
  type, then the folder where you saved the macros would contain
  a file calledMacro1.swpand two
  project folders,Macro1-vbnetand Macro1-csharp. The VB.NET
  and C# projects reside in their respective folders.
  NOTE: TheAutomatically edit
  macro after recordingsystem option has no effect when you select
  to save a just recorded macro asSW All
  Macros Types (*.swp, *.csproj, *.vbproj).

To pause while recording a macro, clickRecord\Pause
MacroorTools,Macro,Pause.
ClickRecord\Pause Macroagain to continue recording.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="EditSolidWorksMacro$$**$$RunSolidWorksMacro$$**$$AssignSolidWorksMacroShortcutKeyMenu$$**$$AssignSolidWorksMacroButton$$**$$VBAMacroOverview$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Record_Solidworks_Macro.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
