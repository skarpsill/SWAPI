---
title: "ModelDoc::SketchConstraintsDel"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchConstraintsDel.htm"
---

# ModelDoc::SketchConstraintsDel

This method is obsolete
and has been superseded by[ModelDoc2::SketchConstraintsDel](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchConstraintsDel.htm).

Description

This method deletes the specified relationship on the currently selected
item.

Syntax (OLE Automation)

void ModelDoc.SketchConstraintsDel
( constrInd, idStr)

(Table)=========================================================

| Input: | (long) constrInd | Constraint number on the selected entity; this is a 0-based index |
| --- | --- | --- |
| Input: | (BSTR) idStr | Constraint to delete |

Syntax (COM)

status = ModelDoc->SketchConstraintsDel
( constrInd, idStr )

(Table)=========================================================

| Input: | (long) constrInd | Constraint number on the selected entity; this is a 0-based index |
| --- | --- | --- |
| Input: | (BSTR) idStr | Constraint to delete |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To delete a tangency relation that is the third relation on the selected
arc, you would specify:

Part.SketchConstraintsDel 2, "sgTANGENT"

The available constraint names used in the idStr argument are as follows.
Embed the string containing the name of the constraint in double quotes.

(Table)=========================================================

| sgHORIZONTAL sgHORIZPOINTS sgVERTICAL sgVERTPOINTS sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT | sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT | sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE |
| --- | --- | --- |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRelation$$**$$ZDeleteRelation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__SketchConstraintsDel.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
