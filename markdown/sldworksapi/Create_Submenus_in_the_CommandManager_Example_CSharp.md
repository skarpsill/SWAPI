---
title: "Create Submenus in the CommandManager Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Submenus_in_the_CommandManager_Example_CSharp.htm"
---

# Create Submenus in the CommandManager Example (C#)

This example shows how to create submenus in the CommandManager framework
by creating individual CommandGroups for each submenu in your tree. Create a C#
addin using the SOLIDWORKS VSTA C# addin template. Set up CommandManager
CommandGroups in SwAddin.ConnectToSW():

public boolConnectToSW(SldWorks
ThisSW, int Cookie)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iApp
= ThisSW;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iCookie
= Cookie;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iApp.SetAddinCallbackInfo2(0, this, iCookie);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iCommand
= iApp.GetCommandManager(iCookie);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SldWorks.CommandGroupcommandGroup = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
title = "CommandGroup1";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
toolTip = "Command group 1 tip";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
hint = "Command group 1 hint";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
position = 6;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup
= iCommand.CreateCommandGroup(CommandGroupID1,
title, toolTip, hint, position);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(commandGroup != null)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BitmapHandler
bitmapHandler = new BitmapHandler();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.LargeIconList= bitmapHandler.CreateFileFromResource("CommandManager.LargeIconList.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.LargeMainIcon= bitmapHandler.CreateFileFromResource("CommandManager.LargeMainIcon.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.SmallIconList= bitmapHandler.CreateFileFromResource("CommandManager.SmallIconList.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.SmallMainIcon= bitmapHandler.CreateFileFromResource("CommandManager.SmallMainIcon.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.ShowInDocumentType= (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeNONE;//
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypePART
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeASSEMBLY
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeDRAWING;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.AddCommandItem2("Command1",
-1, "Command1 hint", "Command1 tool tip", 0, "OnCommand1",
"OnMenuUpdate", 0, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.AddCommandItem2("Command2",
-1, "Command2 hint", "Command2 tool tip", 1, "OnCommand2",
"OnMenuUpdate", 0, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.HasMenu= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.HasToolbar= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.Activate();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup
= null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}title
= "CommandGroup1\\CommandSubGroup1";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}toolTip
= "Command sub group 1 tip";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hint
= "Command sub group 1 hint";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}position
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup
= iCommand.CreateCommandGroup(CommandGroupID2,
title, toolTip, hint, position);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(commandGroup != null)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BitmapHandler
bitmapHandler = new BitmapHandler();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.LargeIconList= bitmapHandler.CreateFileFromResource("CommandManager.LargeIconList.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.LargeMainIcon= bitmapHandler.CreateFileFromResource("CommandManager.LargeMainIcon.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.SmallIconList= bitmapHandler.CreateFileFromResource("CommandManager.SmallIconList.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.SmallMainIcon= bitmapHandler.CreateFileFromResource("CommandManager.SmallMainIcon.bmp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.ShowInDocumentType= (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeNONE;//
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypePART
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeASSEMBLY
|

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeDRAWING;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.AddCommandItem2("SubCommand1",
-1, "Command1 hint", "Command1 tool tip", 0, "OnCommand1",
"OnMenuUpdate", 0, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.AddCommandItem2("SubCommand2",
-1, "Command2 hint", "Command2 tool tip", 1, "OnCommand2",
"OnMenuUpdate", 0, 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.HasMenu= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.HasToolbar= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}commandGroup.Activate();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
true;

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="1217">
<param name="_ExtentY" value="556">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="CommandManager_Object$$**$$CommandGroup_Object$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\sldworksapi\EXAMPLESVB\Create_Submenus_in_the_CommandManager_Example_VB.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
