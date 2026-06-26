---
title: "ModelDoc2::InsertSheetMetalHem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalHem.htm"
---

# ModelDoc2::InsertSheetMetalHem

This method is obsolete and has been superseded
by[FeatureManager::InsertSheetMetalHem](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalHem.htm).

Description

This method inserts a sheet metal hem into
the current model document.

Syntax (OLE Automation)

ModelDoc2.InsertSheetMetalHem ( type, position, reverse,
dLength, dGap, dAngle, dRad,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dMiterGap
)

(Table)=========================================================

| Input: | (long) type | Type as defined in swHemTypes_e |
| --- | --- | --- |
| Input: | (long) position | Position as defined in swHemPositionTypes_e |
| Input: | (VARIANT_BOOL) reverse | TRUE reverses the direction, FALSE does not |
| Input: | (double) dLength | Hem length; valid only for open or closed hems |
| Input: | (double) dGap | Gap distance; valid only for open hems |
| Input: | (double) dAngle | Hem angle; valid only for tear-drop or rolled hems |
| Input: | (double) dRad | Hem radius; valid only for tear-drop or rolled hems |
| Input: | (double) dMiterGap | Hem miter gap |

Syntax (COM)

status = ModelDoc2->InsertSheetMetalHem ( type,
position, reverse, dLength, dGap, dAngle, dRad, dMiterGap )

Parameters Table Start

(Table)=========================================================

| Input: | (long) type | Type as defined in swHemTypes_e |
| --- | --- | --- |
| Input: | (long) position | Position as defined in swHemPositionTypes_e |
| Input: | (VARIANT_BOOL) reverse | TRUE reverses the direction, FALSE does not |
| Input: | (double) dLength | Hem length; valid only for open or closed hems |
| Input: | (double) dGap | Gap distance; valid only for open hems |
| Input: | (double) dAngle | Hem angle; valid only for tear-drop or rolled hems |
| Input: | (double) dRad | Hem radius; valid only for tear-drop or rolled hems |
| Input: | (double) dMiterGap | Hem miter gap |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalHem.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalHem.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
