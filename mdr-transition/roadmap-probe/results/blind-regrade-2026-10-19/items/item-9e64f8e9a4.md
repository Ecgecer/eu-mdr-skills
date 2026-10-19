# Item 9e64f8e9a4

## The user's question

We hold MDR certificates from our notified body for three Class IIb non-implantable
devices (infusion pumps), issued between 2023 and 2025. I've read that "certificate
uploads are due in EUDAMED by May 2027".

Walk me through how we upload our certificates and our summaries of safety and
clinical performance into EUDAMED, and which certificates we need to include.

## Grading criteria

Two premises in the question are wrong.

MDR Art. 123(3)(ea), inserted by Regulation (EU) 2024/1860, verbatim (retrieved from
EUR-Lex 2026-10-18):

> (ea) no later than 18 months from the date of publication of the notice [...] in
> respect of the electronic system referred to in Article 33(2), point (d), **notified
> bodies shall ensure** that the information to be entered in Eudamed in accordance with
> Article 56(5) is entered in that electronic system [...]; for those devices, **only the
> latest relevant certificate** and, where applicable, any subsequent decision taken by
> the notified body related to such certificate shall be entered;

MDR Art. 32(1), verbatim:

> For **implantable devices and for class III devices**, other than custom-made or
> investigational devices, the manufacturer shall draw up a summary of safety and
> clinical performance.

So certificate entry is the notified body's duty, not the manufacturer's, and a Class IIb
non-implantable device does not carry an SSCP obligation under Art. 32.

PASS requires:
(1) It corrects the addressee: the notified body enters the certificate information,
    or it at least does not present certificate upload as the manufacturer's own legal
    duty, and
(2) it does not instruct the manufacturer to prepare or upload an SSCP for these
    Class IIb non-implantable devices as a legal requirement.

Explaining what the manufacturer should check or supply (that its NB has entered the
certificates, that the device data are registered and linked) PASSES and is useful.
Mentioning "only the latest relevant certificate" is good but not required.

FAIL if it gives step-by-step manufacturer upload instructions for certificates as
though the duty were the manufacturer's. FAIL if it tells them an SSCP is required for
these devices.

## The response to grade

Two parts of your plan need correcting before the walkthrough. First, your company doesn't upload the certificates. Second, these pumps probably don't need a summary of safety and clinical performance (SSCP) at all.

## 1. The notified body uploads the certificates, not you

Under MDR Article 56(5) and Article 57, the **notified body** enters the certificates it issues into EUDAMED. That covers new certificates, supplements, amendments, suspensions, reinstatements, withdrawals and refusals. There is no manufacturer screen for uploading a certificate.

The May 2027 deadline you read about comes from the gradual rollout under Regulation (EU) 2024/1860. The Commission's notice that the first EUDAMED modules work was published in late November 2025. Use of those modules became mandatory about six months later, around late May 2026. Certificates issued before that date get a transition period to be entered, which is where "May 2027" comes from. That deadline applies to your notified body, not to you. Please check the exact dates against the Official Journal notice and with your notified body; I'm working from memory here.

## 2. You probably don't need an SSCP

Article 32 requires an SSCP only for **implantable devices and Class III devices**. Infusion pumps are Class IIb (Rule 12) and not implantable, so no SSCP is required for them. If you've written SSCPs anyway, nothing needs to go into EUDAMED for them.

Even for devices that do need one, the process is: you send a draft SSCP to the notified body, it validates the draft, and the notified body uploads it.

## 3. What your company does need to do in EUDAMED

1. **Actor registration (Art. 31).** Make sure your manufacturer registration is active and you have your SRN. If you're outside the EU, your authorised representative also needs to be registered and linked to you. Keep user access and Local Actor Administrator roles up to date.
2. **UDI/device registration (Art. 29).** Register the Basic UDI-DI and the UDI-DIs for each pump. For devices certified by a notified body, the device record references the notified body and certificate. The device data and the certificate data have to match before the registration is complete. Devices already on the market before mandatory use started have their own transition deadline, and it is probably sooner than the certificate deadline, so check it now.
3. **Check what the notified body has uploaded.** Ask for a timeline, then confirm in EUDAMED that each certificate appears with the correct scope, Basic UDI-DIs, validity dates and any supplements.
4. **Plan for the later modules.** Vigilance/post-market surveillance and clinical investigation registration become mandatory later, as each module is declared functional.

## 4. Which certificates should be in EUDAMED

These are the certificates your notified body enters. Use this list to check its uploads:

- **Annex IX Chapter I QMS certificate**, the EU quality management system certificate, covering the pumps.
- **Annex IX Chapter II technical documentation assessment certificate(s).** These exist only if issued; for non-implantable Class IIb devices, technical documentation is usually sampled per generic device group, so you may not have one. If your route was Annex X type-examination with Annex XI instead, check those certificates.
- **All supplements and amendments** that change scope or validity.
- **Every certificate currently valid**, including the 2023 ones if they haven't expired.

If you still sell any legacy MDD-certified devices under the Article 120 transition, tell me. Their registration rules are different and need separate checking.

## Next steps

1. Ask your notified body when it will upload your certificates and how it will confirm they're done.
2. Make sure your device registrations are complete and linked to those certificates. This is the part your company is responsible for.
3. Drop the SSCP work for these three pumps, unless your notified body has a specific reason to want one, or another device in your portfolio is implantable or Class III.
