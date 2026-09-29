from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from escolas.models import Escola
from .models import Usuario


class AreaPessoalTests(TestCase):
	def test_area_pessoal_abre_sem_perfil_cadastral(self):
		usuario = get_user_model().objects.create_user(username='leitora', password='senha-segura-123')
		self.client.force_login(usuario)

		resposta = self.client.get(reverse('minha_area'))

		self.assertEqual(resposta.status_code, 200)
		self.assertContains(resposta, 'Meus favoritos')
		self.assertContains(resposta, 'Meus comentários')
		
class GestaoUsuariosTests(TestCase):
	def setUp(self):
		self.administrador = get_user_model().objects.create_superuser(
			username='admin',
			email='admin@example.test',
			password='senha-segura-123',
		)
		self.escola = Escola.objects.create(nome='Escola teste', cidade='Recife', estado='PE')
		self.client.force_login(self.administrador)

	def test_lista_e_cadastro_de_usuario_usam_perfil_separado(self):
		resposta = self.client.get(reverse('listar_usuarios'))
		self.assertEqual(resposta.status_code, 200)

		resposta = self.client.post(reverse('criar_usuario'), {
			'username': 'nova_leitora',
			'password': 'senha-segura-456',
			'data_nasc': '2005-06-15',
			'rg': '1234567',
			'cpf': '123.456.789-01',
			'escola': self.escola.pk,
		})

		self.assertRedirects(resposta, reverse('listar_usuarios'))
		perfil = Usuario.objects.select_related('user').get(user__username='nova_leitora')
		self.assertTrue(perfil.user.check_password('senha-segura-456'))
