import random
from faker import Faker
# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

from intake.constants import GENDER_PRONOUN_CHOICES

# create new provider class


class Provider(BaseProvider):

    def some_choice(self, choices):
        return random.choice(
            [key for key, display in choices])

    def maybe(self, chance_of_yes=0.5):
        return self.random_element({
            "yes": chance_of_yes,
            "no": 1.0 - chance_of_yes})

    def generate_contact_preferences(self):
        preferences = random.randint(1, 4)
        return random.sample([
            'prefers_email',
            'prefers_sms',
            'prefers_snailmail',
            'prefers_voicemail',
            ], preferences)

    def make_phone_number(self):
        return self.numerify('2##-###-####')

    def sf_county_form_answers(self, **overrides):
        data = {
            'first_name': self.generator.first_name(),
            'middle_name': self.generator.first_name(),
            'last_name': self.generator.last_name(),
            'contact_preferences': self.generate_contact_preferences(),
            'phone_number': self.make_phone_number(),
            'email': self.generator.free_email(),
            'address.street': self.generator.street_address(),
            'address.city': self.generator.city(),
            'address.state': self.generator.state_abbr(),
            'address.zip': self.generator.zipcode(),
            'being_charged': self.maybe(0.05),
            'currently_employed': self.maybe(0.4),
            'dob.day': str(random.randint(1, 31)),
            'dob.month': str(random.randint(1, 12)),
            'dob.year': str(random.randint(1959, 2000)),
            'monthly_income': str(random.randint(100, 7000)),
            'monthly_expenses': str(random.randint(100, 3000)),
            'rap_outside_sf': self.maybe(0.1),
            'serving_sentence': self.maybe(0.05),
            'ssn': self.numerify('#########'),
            'us_citizen': self.maybe(0.8),
            'on_probation_parole': self.maybe(0.1),
            'when_probation_or_parole': '',
            'when_where_outside_sf': '',
            'where_probation_or_parole': '',
            'consent_to_represent': 'yes',
            'understands_limits': 'yes',
            'how_did_you_hear': '',
            'additional_information': 'I want help',
        }
        data.update(overrides)
        return data

    def contra_costa_county_form_answers(self, **overrides):
        data = {
            'contact_preferences': self.generate_contact_preferences(),
            'first_name': self.generator.first_name(),
            'last_name': self.generator.last_name(),
            'phone_number': self.make_phone_number(),
            'email': self.generator.free_email(),
            'dob.day': str(random.randint(1, 31)),
            'dob.month': str(random.randint(1, 12)),
            'dob.year': str(random.randint(1959, 2000)),
            'us_citizen': self.maybe(0.8),
            'address.street': self.generator.street_address(),
            'address.city': self.generator.city(),
            'address.state': self.generator.state_abbr(),
            'address.zip': self.generator.zipcode(),
            'on_probation_parole': self.maybe(0.1),
            'serving_sentence': self.maybe(0.05),
            'currently_employed': self.maybe(0.4),
            'monthly_income': str(random.randint(100, 7000)),
            'monthly_expenses': str(random.randint(100, 3000)),
            'income_source': 'a job',
            'consent_to_represent': 'yes',
            'understands_limits': 'yes',
            'how_did_you_hear': '',
            'additional_information': '',
        }
        data.update(overrides)
        return data

    def alameda_county_form_answers(self, **overrides):
        data = {
            'contact_preferences': self.generate_contact_preferences(),
            # 'preferred_pronouns': self.some_choice(GENDER_PRONOUN_CHOICES),
            'first_name': self.generator.first_name(),
            'middle_name': self.generator.first_name(),
            'last_name': self.generator.last_name(),
            'phone_number': self.make_phone_number(),
            'alternate_phone_number': self.make_phone_number(),
            'email': self.generator.free_email(),
            'dob.day': str(random.randint(1, 31)),
            'dob.month': str(random.randint(1, 12)),
            'dob.year': str(random.randint(1959, 2000)),
            'us_citizen': self.maybe(0.8),
            'address.street': self.generator.street_address(),
            'address.city': self.generator.city(),
            'address.state': self.generator.state_abbr(),
            'address.zip': self.generator.zipcode(),
            'on_probation_parole': 'yes',
            'rap_outside_sf': self.maybe(0.1),
            'finished_half_probation': 'not_applicable',
            'reduced_probation': 'not_applicable',
            'being_charged': self.maybe(0.05),
            'serving_sentence': self.maybe(0.05),
            'has_suspended_license': self.maybe(0.3),
            'owes_court_fees': self.maybe(0.4),
            'monthly_income': str(random.randint(100, 7000)),
            'on_public_benefits': self.maybe(0.7),
            'owns_home': self.maybe(0.1),
            'household_size': str(random.randint(0, 4)),
            'consent_to_represent': 'yes',
            'understands_limits': 'yes',
            'how_did_you_hear': 'from work',
            'additional_information': 'I want help',
        }
        data.update(overrides)
        return data

    def declaration_letter_answers(self, **overrides):
        data = {
            'declaration_letter_intro': self.generator.paragraph(3, True),
            'declaration_letter_life_changes': self.generator.paragraph(
                3, True),
            'declaration_letter_activities': self.generator.paragraph(3, True),
            'declaration_letter_goals': self.generator.paragraph(3, True),
            'declaration_letter_why': self.generator.paragraph(3, True),
        }
        data.update(overrides)
        return data

    def other_county_answers(self, **overrides):
        data = {
            'contact_preferences': self.generate_contact_preferences(),
            'first_name': self.generator.first_name(),
            'phone_number': self.make_phone_number(),
            'email': self.generator.free_email(),
            'address.street': self.generator.street_address(),
            'address.city': self.generator.city(),
            'address.state': self.generator.state_abbr(),
            'address.zip': self.generator.zipcode(),
            'how_did_you_hear': '',
        }
        data.update(overrides)
        return data

    def cleaned_sf_county_form_answers(self, **overrides):
        data = {
            'first_name': self.generator.first_name(),
            'middle_name': self.generator.first_name(),
            'last_name': self.generator.last_name(),
            'contact_preferences': self.generate_contact_preferences(),
            'phone_number': self.make_phone_number(),
            'email': self.generator.free_email(),
            'address': {
                'street': self.generator.street_address(),
                'city': self.generator.city(),
                'state': self.generator.state_abbr(),
                'zip': self.generator.zipcode(),
            },
            'being_charged': self.maybe(0.05),
            'currently_employed': self.maybe(0.4),
            'dob': {
                'day': str(random.randint(1, 31)),
                'month': str(random.randint(1, 12)),
                'year': str(random.randint(1959, 2000)),
            },
            'monthly_expenses': str(random.randint(100, 3000)),
            'monthly_income': str(random.randint(100, 7000)),
            'rap_outside_sf': self.maybe(0.1),
            'serving_sentence': self.maybe(0.05),
            'ssn': self.numerify('#########'),
            'us_citizen': self.maybe(0.8),
            'on_probation_parole': self.maybe(0.1),
            'when_probation_or_parole': '',
            'when_where_outside_sf': '',
            'where_probation_or_parole': '',
            'how_did_you_hear': '',
            'consent_to_represent': 'yes',
            'understands_limits': 'yes',
            'additional_information': 'I want help',
        }
        data.update(overrides)
        return data

    def ebclc_answers(self, **overrides):
        data = self.alameda_county_form_answers()
        data['monthly_income'] = 3001
        data['owns_home'] = "yes"
        data.update(overrides)
        return data

    def alameda_pubdef_answers(self, **overrides):
        data = self.alameda_county_form_answers()
        data['monthly_income'] = 2999
        data['owns_home'] = "no"
        data.update(overrides)
        return data

    def monterey_pubdef_answers(self, **overrides):
        data = self.alameda_county_form_answers()
        data.update(
            is_veteran=self.maybe(0.1),
            is_student=self.maybe(0.2),
            when_probation_or_parole='2018',
            where_probation_or_parole='Solano County',
        )
        data.update(overrides)
        return data

    def solano_pubdef_answers(self, **overrides):
        data = self.monterey_pubdef_answers()
        data.update(
            owes_court_fees=self.maybe(0.5),
        )
        data.update(overrides)
        return data

    def san_diego_pubdef_answers(self, **overrides):
        data = self.solano_pubdef_answers()
        data.update(
            case_number=self.generator.numerify("C####-###"),
            reasons_for_applying=['background_check', 'lost_job', 'housing'],
        )
        data.update(overrides)
        return data

    def san_joaquin_pubdef_answers(self, **overrides):
        return self.solano_pubdef_answers(**overrides)

    def santa_clara_pubdef_answers(self, **overrides):
        data = self.solano_pubdef_answers()
        data.update(
            currently_employed=self.maybe(0.3),
            income_source='a job',
            monthly_expenses=2000,
            is_married=self.maybe(0.4),
            has_children=self.maybe(0.6),
            reduced_probation=self.maybe(0.1),
            reasons_for_applying=['background_check', 'lost_job', 'housing'],
        )
        data.update(overrides)
        return data

    def fresno_pubdef_answers(self, **overrides):
        data = self.solano_pubdef_answers()
        data.update(
            aliases=self.generator.name(),
            driver_license_or_id=self.generator.numerify("D#######"),
            last_four=self.generator.numerify("####"),
            case_number=self.generator.numerify("C####-###"),
            dependents=random.randint(0, 5),
            reasons_for_applying=['background_check', 'lost_job', 'housing'],
        )
        data.update(overrides)
        return data

    def all_county_answers(self, **overrides):
        data = {
            **self.sf_county_form_answers(),
            **self.alameda_county_form_answers(),
            **self.contra_costa_county_form_answers(),
            **self.monterey_pubdef_answers(),
            **self.san_joaquin_pubdef_answers(),
            **self.san_diego_pubdef_answers(),
            **self.santa_clara_pubdef_answers(),
            **self.fresno_pubdef_answers(),
        }
        data.update(overrides)
        return data
