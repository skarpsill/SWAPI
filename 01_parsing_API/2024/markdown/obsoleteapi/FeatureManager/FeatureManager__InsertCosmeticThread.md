---
title: "FeatureManager::InsertCosmeticThread"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertCosmeticThread.htm"
---

# FeatureManager::InsertCosmeticThread

This method is obsolete and has been superseded
by[FeatureManager::InsertCosmeticThread2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertCosmeticThread2.htm).

Description

This method inserts a cosmetic
thread.

Syntax (OLE Automation)

retval = FeatureManager.InsertCosmeticThread ( type,
depth, length, note )

(Table)=========================================================

| Input: | (short) type | Type as defined in swCosmeticThreadType_e |
| --- | --- | --- |
| Input: | (double) depth | Diameter of the cosmetic thread |
| Input: | (double) length | Length of the cosmetic thread |
| Input: | (BSTR) note | Callout text to display in the drawing document |
| Output: | (BSTR) retval | Name of the cosmetic thread feature |

Syntax (COM)

status = FeatureManager->InsertCosmeticThread
( type, depth, length, note, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (short) type | Type as defined in swCosmeticThreadType_e |
| --- | --- | --- |
| Input: | (double) depth | Diameter of the cosmetic thread |
| Input: | (double) length | Length of the cosmetic thread |
| Input: | (BSTR) note | Callout text to display in the drawing document |
| Output: | (BSTR) retval | Name of the cosmetic thread feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the name
of the cosmetic thread feature, which you can use to retrieve the cosmetic
thread feature in a part or assembly or the cosmetic thread annotation
in a drawing.

(Table)=========================================================

| In a... | You... |
| --- | --- |
| Part - or - Assembly | Use PartDoc::FeatureByName - or - Use AssemblyDoc::FeatureByName |
| Drawing | Search through the cosmetic threads of the drawing views for the annotation
by that name using Annotation::GetName |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertCosmeticThread.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="FeatureManager_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertCosmeticThread.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
