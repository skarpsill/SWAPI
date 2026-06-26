---
title: "FeatureManager::InsertMoveCopyBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/FeatureManager__InsertMoveCopyBody.htm"
---

# FeatureManager::InsertMoveCopyBody

This method is obsolete and has been superseded
by[FeatureManager::InsertMoveCopyBody2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMoveCopyBody2.htm).

Description

This method moves, rotates,
and makes copies of the selected solid bodies or surfaces.

Syntax (OLE Automation)

retval = FeatureManager.InsertMoveCopyBody ( transX,
transY, transZ, transDist, rotPointX, rotPointY, rotPointZ, rotAngleX,
rotAngleY, rotAngleZ, bCopy, numCopies )

(Table)=========================================================

| Input: | (double) transX | Value for delta X; applies to translation |
| --- | --- | --- |
| Input: | (double) transY | Value for delta Y; applies to translation |
| Input: | (double) transZ | Value for delta Z; applies to translation |
| Input: | (double) transDist | Distance; applies to translation |
| Input: | (double) rotPointX | Value for X rotation origin; applies to rotation |
| Input: | (double) rotPointY | Value for Y rotation origin; applies to rotation |
| Input: | (double) rotPointZ | Value for Z rotation origin; applies to rotation |
| Input: | (double) rotAngleX | Value for X rotation angle; applies to rotation |
| Input: | (double) rotAngleY | Value for Y rotation angle; applies to rotation |
| Input: | (double) rotAngleZ | Value for Z rotation angle; applies to rotation |
| Input: | (VARIANT_BOOL) bCopy | TRUE if a copy operation, FALSE if a move operation |
| Input: | (long) numCopies | Number of copies to create |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertMoveCopyBody (
transX, transY, transZ, transDist, rotPointX, rotPointY, rotPointZ, rotAngleX,
rotAngleY, rotAngleZ, bCopy, numCopies, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (double) transX | Value for delta X; applies to translation |
| --- | --- | --- |
| Input: | (double) transY | Value for delta Y; applies to translation |
| Input: | (double) transZ | Value for delta Z; applies to translation |
| Input: | (double) transDist | Distance; applies to translation |
| Input: | (double) rotPointX | Value for X rotation origin; applies to rotation |
| Input: | (double) rotPointY | Value for Y rotation origin; applies to rotation |
| Input: | (double) rotPointZ | Value for Z rotation origin; applies to rotation |
| Input: | (double) rotAngleX | Value for X rotation angle; applies to rotation |
| Input: | (double) rotAngleY | Value for Y rotation angle; applies to rotation |
| Input: | (double) rotAngleZ | Value for Z rotation angle; applies to rotation |
| Input: | (VARIANT_BOOL) bCopy | TRUE if a copy operation, FALSE if a move operation |
| Input: | (long) numCopies | Number of copies to create |
| Output: | (LPFEATURE) retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method applies either
to the specified translation or rotation. If you specify both translation
and rotation, only the translation is applied.

See theInsert,
Surface, Move/Copycommand in the SolidWorks Help for details about
moving, rotating, and copying solid bodies and surfaces.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\SldWorks\FeatureManager__InsertMoveCopyBody.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$PartDoc::InsertPart$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\SldWorks\FeatureManager__InsertMoveCopyBody.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
